#!/usr/bin/env bash
# Start the project IDE (the File Tree page and its server) on this machine.
#
#   ./start.sh            sync with git, stop the old server, rebuild the page data, start it, check that it answers
#   ./start.sh --no-pull  the same without the git sync
#   ./start.sh stop       stop the server
#   ./start.sh status     is it running, and what its health check says
#   ./start.sh logs       follow the server's log
#   ./start.sh serve      what the service runs at boot: sync, rebuild, then the server in the foreground
#
# Run ./init.sh once first: it installs what the server needs and the service that starts it at boot.
# The server listens only on 127.0.0.1; reach it from your computer with an SSH tunnel (apps/project-IDE/server/README.md).
set -u

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SERVICE=project-ide
UNIT="$HOME/.config/systemd/user/$SERVICE.service"
SERVER="$ROOT/apps/project-IDE/server/server.py"
REBUILD="$ROOT/agents/system/.claude/skills/ide-build/scripts/rebuild.py"
STORE="$ROOT/apps/project-IDE/data/page-store"
RUN_DIR="$ROOT/agents/system/logs/services/$SERVICE"   # run-time files; git ignores them
PID_FILE="$RUN_DIR/server.pid"
LOG_FILE="$RUN_DIR/server.log"
# files the build writes; they are rebuilt after the sync, so a local copy never blocks a pull
GENERATED=(apps/project-IDE/current-ui/file-tree.data.json apps/project-IDE/current-ui/real-files.json docs/file-tree.md)

PY="$ROOT/.venv/bin/python"
[ -x "$PY" ] || PY=$(command -v python3)
PORT=${IDE_PORT:-$("$PY" -c 'import json,sys; print(json.load(open(sys.argv[1])).get("port", 8765))' "$ROOT/apps/project-IDE/server/server.config.json" 2>/dev/null || echo 8765)}
URL="http://127.0.0.1:$PORT"

say()  { printf '%s\n' "$*"; }
warn() { printf 'warning: %s\n' "$*" >&2; }
has_unit() { [ -f "$UNIT" ] && systemctl --user cat "$SERVICE" >/dev/null 2>&1; }
healthy() { curl -fsS --max-time 3 "$URL/api/health" 2>/dev/null; }

# ---------- 1. sync: bring the remote branch in, when that is safe ----------
sync() {
    cd "$ROOT" || return 1
    local branch upstream behind ahead dirty
    branch=$(git symbolic-ref --short -q HEAD) || { warn "detached HEAD; git sync skipped"; return 0; }
    upstream=$(git rev-parse --abbrev-ref -q "$branch@{u}" 2>/dev/null) || { say "sync: $branch has no upstream; skipped"; return 0; }
    if ! GIT_TERMINAL_PROMPT=0 timeout 60 git fetch -q "${upstream%%/*}"; then
        warn "git fetch failed (offline?); starting with what is on disk"; return 0
    fi
    read -r ahead behind < <(git rev-list --left-right --count "HEAD...$upstream")
    if [ "$behind" -eq 0 ]; then
        say "sync: $branch is up to date with $upstream$([ "$ahead" -gt 0 ] && echo " ($ahead local commits not pushed)")"
    else
        git checkout -q -- "${GENERATED[@]}" 2>/dev/null   # rebuilt in step 3 anyway
        dirty=$(git status --porcelain --untracked-files=no)
        if [ "$ahead" -ne 0 ]; then
            warn "sync: $branch and $upstream have both moved ($ahead local, $behind remote commits); pull skipped, merge by hand"
        elif [ -n "$dirty" ]; then
            warn "sync: $behind new commits on $upstream, but these local changes are not committed; pull skipped:"
            printf '  %s\n' "$dirty" >&2
        else
            git merge -q --ff-only "$upstream" && say "sync: pulled $behind commits from $upstream"
        fi
    fi
    # what the owner left on the page and nobody has synced yet
    local waiting
    waiting=$(find "$STORE/nodes" -name '*.json' 2>/dev/null | wc -l)
    [ "$waiting" -gt 0 ] && say "sync: $waiting items on the page are marked changed; press Apply changes on the page, or say \"sync the file tree\" to Claude Code"
    return 0
}

# ---------- 2. stop: the service, and any server left from a manual start ----------
stop_strays() {   # with "pidfile": also the server started in the background by an earlier ./start.sh
    local pids pid
    pids=$( { [ "${1:-}" = pidfile ] && cat "$PID_FILE" 2>/dev/null; lsof -t -iTCP:"$PORT" -sTCP:LISTEN 2>/dev/null; } | sort -u)
    for pid in $pids; do
        # only our own server, never another program on the port
        if tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null | grep -q "project-IDE/server/server.py"; then
            say "stop: server process $pid"
            kill "$pid" 2>/dev/null
            for _ in 1 2 3 4 5 6 7 8 9 10; do kill -0 "$pid" 2>/dev/null || break; sleep 0.5; done
            kill -0 "$pid" 2>/dev/null && kill -9 "$pid" 2>/dev/null
        fi
    done
    [ "${1:-}" = pidfile ] && rm -f "$PID_FILE"
    if lsof -t -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
        warn "port $PORT is held by another program; the server cannot start"; return 1
    fi
}

stop() {
    if has_unit && systemctl --user is-active -q "$SERVICE"; then
        say "stop: service $SERVICE"
        systemctl --user stop "$SERVICE"
    fi
    stop_strays pidfile
}

# ---------- 3. rebuild the page data ----------
rebuild() {
    say "rebuild:"
    "$PY" "$REBUILD" || warn "the rebuild reported a problem; the server starts with the data on disk"
}

# ---------- 4. serve: the foreground process the service runs ----------
serve() {
    [ "${NO_PULL:-}" = 1 ] || sync
    stop_strays || exit 1
    rebuild
    say "serve: $URL/ (python $("$PY" -c 'import sys; print(sys.version.split()[0])'))"
    cd "$ROOT" && exec "$PY" -u "$SERVER"
}

# ---------- start: hand over to the service (or the background), then wait until it answers ----------
start() {
    mkdir -p "$RUN_DIR"
    stop || exit 1
    local follower
    if has_unit; then
        say "start: service $SERVICE (it syncs, rebuilds and serves; its output follows)"
        journalctl --user -u "$SERVICE" -f -n 0 -o cat 2>/dev/null & follower=$!
        if [ "${NO_PULL:-}" = 1 ]; then systemctl --user set-environment NO_PULL=1; else systemctl --user unset-environment NO_PULL; fi
        systemctl --user start "$SERVICE"
    else
        say "start: in the background (no service installed; run ./init.sh for a start at boot)"
        : > "$LOG_FILE"
        NO_PULL=${NO_PULL:-} nohup "$ROOT/start.sh" serve >> "$LOG_FILE" 2>&1 < /dev/null &
        echo $! > "$PID_FILE"
        tail -n +1 -f "$LOG_FILE" & follower=$!
    fi
    local health=""
    for _ in $(seq 1 120); do
        health=$(healthy) && break
        has_unit && [[ $(systemctl --user show -p ActiveState --value "$SERVICE") =~ ^(failed|inactive)$ ]] && break
        sleep 1
    done
    sleep 0.3; kill "$follower" 2>/dev/null; wait "$follower" 2>/dev/null
    has_unit && systemctl --user unset-environment NO_PULL
    if [ -n "$health" ]; then
        say ""
        say "The project IDE runs at $URL/  health: $health"
        say "From your computer: ssh -N -L $PORT:127.0.0.1:$PORT $(id -un)@<this server>, then open http://127.0.0.1:$PORT/"
    else
        warn "the server did not answer at $URL/api/health; see ./start.sh logs"; exit 1
    fi
}

status() {
    if has_unit; then systemctl --user --no-pager status "$SERVICE" | head -5; else say "service: not installed (./init.sh)"; fi
    if h=$(healthy); then say "health: $h"; else say "health: no answer at $URL"; exit 1; fi
}

logs() {
    if has_unit; then journalctl --user -u "$SERVICE" -f -o cat; else tail -f "$LOG_FILE"; fi
}

case "${1:-}" in
    ""|start)  start ;;
    --no-pull) NO_PULL=1; export NO_PULL; start ;;
    serve)     serve ;;
    stop)      stop ;;
    status)    status ;;
    logs)      logs ;;
    -h|--help) sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//' ;;
    *)         sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'; exit 2 ;;
esac
