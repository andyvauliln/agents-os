#!/usr/bin/env bash
# Set up this machine once to run the project IDE, then start it.
#
#   ./init.sh             check the tools, install the Python package the request box needs into .venv/,
#                         install the service that starts the IDE at boot, and run ./start.sh
#   ./init.sh --no-service   the same without the service (start it by hand with ./start.sh)
#
# Safe to run again: it only adds what is missing and writes the service file anew.
# It never reads or writes a keys file; the server reads the keys it names itself (apps/project-IDE/server/README.md).
set -u

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SERVICE=project-ide
UNIT_DIR="$HOME/.config/systemd/user"
UNIT="$UNIT_DIR/$SERVICE.service"
VENV="$ROOT/.venv"

say()  { printf '%s\n' "$*"; }
warn() { printf 'warning: %s\n' "$*" >&2; }
die()  { printf 'error: %s\n' "$*" >&2; exit 1; }

# ---------- 1. the tools ----------
say "1. tools"
command -v git >/dev/null || die "git is missing"
command -v curl >/dev/null || die "curl is missing"
command -v python3 >/dev/null || die "python3 is missing (3.10 or newer)"
python3 -c 'import sys; sys.exit(sys.version_info < (3, 10))' || die "python3 is $(python3 -V); 3.10 or newer is needed"
say "   python $(python3 -c 'import sys; print(sys.version.split()[0])'), git $(git --version | cut -d' ' -f3)"
if command -v node >/dev/null; then say "   node $(node --version)"; else warn "node is missing: Claude Code and the page check need it"; fi
if command -v claude >/dev/null; then
    say "   claude $(claude --version 2>/dev/null | head -1)"
else
    warn "Claude Code is missing (npm install -g @anthropic-ai/claude-code): the page works, the request box stays off"
fi

# ---------- 2. the Python package of the request box, in .venv/ (git ignores it) ----------
say "2. python packages in .venv/"
if [ ! -x "$VENV/bin/python" ]; then
    if command -v uv >/dev/null; then uv venv -q "$VENV"
    elif python3 -m venv "$VENV" 2>/dev/null; then :
    elif command -v virtualenv >/dev/null; then virtualenv -q "$VENV"
    else die "cannot make $VENV: install uv, python3-venv or virtualenv"
    fi
fi
if ! "$VENV/bin/python" -c 'import claude_agent_sdk' 2>/dev/null; then
    if command -v uv >/dev/null; then uv pip install -q --python "$VENV/bin/python" claude-agent-sdk
    else "$VENV/bin/python" -m pip install -q claude-agent-sdk
    fi || die "could not install claude-agent-sdk"
fi
say "   claude-agent-sdk $("$VENV/bin/python" -c 'from importlib.metadata import version; print(version("claude-agent-sdk"))')"

# ---------- 3. the service that starts the IDE at boot ----------
say "3. start at boot"
if [ "${1:-}" = "--no-service" ]; then
    say "   skipped (--no-service)"
elif ! systemctl --user show-environment >/dev/null 2>&1; then
    warn "no systemd user session here: the IDE does not start at boot; start it with ./start.sh"
else
    mkdir -p "$UNIT_DIR"
    # the service gets the PATH and Claude Code settings folder of the person who runs init.sh,
    # so it finds node and claude and uses the same sign-in
    path=$(printf '%s' "$PATH" | tr ':' '\n' | grep -v -e '\.cursor-server' -e '\.vscode-server' | paste -sd: -)
    {
        echo "# Written by $ROOT/init.sh; run it again to rewrite. Logs: journalctl --user -u $SERVICE -f"
        echo "[Unit]"
        echo "Description=Agent OS project IDE: the File Tree page and its server ($ROOT)"
        echo "After=network-online.target"
        echo "Wants=network-online.target"
        echo ""
        echo "[Service]"
        echo "Type=simple"
        echo "WorkingDirectory=$ROOT"
        echo "Environment=\"PATH=$path\""
        [ -n "${CLAUDE_CONFIG_DIR:-}" ] && echo "Environment=\"CLAUDE_CONFIG_DIR=$CLAUDE_CONFIG_DIR\""
        echo "ExecStart=/bin/bash $ROOT/start.sh serve"
        echo "Restart=on-failure"
        echo "RestartSec=10"
        echo "# the sync can wait on the network and the rebuild takes a few seconds"
        echo "TimeoutStartSec=180"
        echo "# stopping the service also stops every Claude Code run it started"
        echo "KillMode=control-group"
        echo "TimeoutStopSec=30"
        echo ""
        echo "[Install]"
        echo "WantedBy=default.target"
    } > "$UNIT"
    systemctl --user daemon-reload
    systemctl --user enable -q "$SERVICE"
    say "   service $SERVICE installed and enabled ($UNIT)"
    if [ "$(loginctl show-user "$(id -un)" -p Linger --value 2>/dev/null)" = yes ]; then
        say "   lingering is on: the service starts at boot, before anyone logs in"
    elif loginctl enable-linger "$(id -un)" 2>/dev/null; then
        say "   lingering turned on: the service starts at boot, before anyone logs in"
    else
        warn "the service starts only when $(id -un) logs in; for a start at boot run: sudo loginctl enable-linger $(id -un)"
    fi
fi

# ---------- 4. start it ----------
say "4. start"
exec "$ROOT/start.sh"
