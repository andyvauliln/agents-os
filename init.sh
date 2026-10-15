#!/usr/bin/env bash
# Set up this machine once to run the project IDE, then start it.
#
#   ./init.sh             check the tools, install the Python package the request box needs into .venv/,
#                         install the service that starts the IDE at boot, and run ./start.sh
#   ./init.sh --no-service   the same without the service (start it by hand with ./start.sh)
# It also finds a browser for the page check (check_page.js) and writes where it is to .playwright.env.
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

# ---------- 4. the browser for the page check (check_page.js), found once and written to .playwright.env ----------
say "4. browser for the page check"
browser_setup() {
    local mod="" chrome="" libs="$HOME/.local/share/agent-os/browser-libs" missing pkg lib i
    # the Playwright module: a global one, or one another project on this machine already has
    for d in "$(npm root -g 2>/dev/null)/playwright" "$(npm root -g 2>/dev/null)/playwright-core" /opt/node22/lib/node_modules/playwright; do
        [ -f "$d/package.json" ] && { mod=$d; break; }
    done
    [ -n "$mod" ] || mod=$(find "$HOME" -maxdepth 5 -type d \( -path '*/node_modules/playwright-core' -o -path '*/node_modules/playwright' \) -not -path '*/.cache/*' -not -path '*/.npm/*' 2>/dev/null | head -1)
    if [ -z "$mod" ] && command -v npm >/dev/null; then
        npm install -s --prefix "$HOME/.local/share/agent-os/playwright" playwright-core >/dev/null 2>&1 && mod="$HOME/.local/share/agent-os/playwright/node_modules/playwright-core"
    fi
    [ -n "$mod" ] || { warn "no Playwright module found: the page check (check_page.js) cannot run here"; return 0; }
    # the browser: the newest headless Chromium Playwright downloaded, else the full one
    chrome=$(ls -d "$HOME"/.cache/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell 2>/dev/null | sort -V | tail -1)
    [ -n "$chrome" ] || chrome=$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux*/chrome 2>/dev/null | sort -V | tail -1)
    if [ -z "$chrome" ]; then
        (cd "$(dirname "$mod")/.." && node "$mod/cli.js" install chromium-headless-shell >/dev/null 2>&1)
        chrome=$(ls -d "$HOME"/.cache/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell 2>/dev/null | sort -V | tail -1)
    fi
    [ -n "$chrome" ] || { warn "no Chromium found: the page check cannot run here"; return 0; }
    # libraries the system lacks: unpacked from their packages into our own folder, without sudo
    for i in 1 2 3 4 5; do
        missing=$(LD_LIBRARY_PATH="$libs/root/usr/lib/x86_64-linux-gnu" ldd "$chrome" 2>/dev/null | awk '/not found/{print $1}')
        [ -z "$missing" ] && break
        command -v apt-get >/dev/null || { warn "missing browser libraries ($missing) and no apt-get to fetch them"; break; }
        mkdir -p "$libs/deb"
        for lib in $missing; do
            pkg=$(printf '%s' "$lib" | sed -E 's/\.so\.?([0-9]*).*/\1/')   # libgbm.so.1 -> libgbm1, libwayland-server.so.0 -> libwayland-server0
            (cd "$libs/deb" && apt-get download -q "$pkg" >/dev/null 2>&1) || warn "could not fetch $pkg for $lib"
        done
        for f in "$libs"/deb/*.deb; do [ -f "$f" ] && dpkg -x "$f" "$libs/root"; done
    done
    local libdir=""
    [ -d "$libs/root/usr/lib/x86_64-linux-gnu" ] && libdir="$libs/root/usr/lib/x86_64-linux-gnu"
    if LD_LIBRARY_PATH="$libdir" "$chrome" --headless --no-sandbox --dump-dom about:blank >/dev/null 2>&1; then
        printf 'PLAYWRIGHT=%s\nCHROMIUM=%s\nPLAYWRIGHT_LIBS=%s\n' "$mod" "$chrome" "$libdir" > "$ROOT/.playwright.env"
        say "   page check ready: $(basename "$(dirname "$chrome")") with $(basename "$mod") ($ROOT/.playwright.env)"
    else
        warn "Chromium does not start here; the page check cannot run (try: sudo npx playwright install-deps chromium)"
    fi
}
browser_setup

# ---------- 5. start it ----------
say "5. start"
exec "$ROOT/start.sh"
