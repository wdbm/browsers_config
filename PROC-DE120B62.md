# PROC-DE120B62

This procedure is to make available to a coding agent the MCP of a local Firefox installation which was set up using a procedure like [PROC-905A9EDF](PROC-905A9EDF.py).

```Bash
# Install `nvm` and Node.js at user level.
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.7/install.sh | bash
source "${HOME}/.bashrc"
nvm install 24
nvm alias default 24
nvm use 24

# Register the local Firefox MCP with a coding agent.
$CODEX_BIN mcp add firefox-devtools \
    --env "DISPLAY=${DISPLAY}" \
    --env "WAYLAND_DISPLAY=${WAYLAND_DISPLAY}" \
    --env "XDG_RUNTIME_DIR=${XDG_RUNTIME_DIR}" \
    -- \
    npx -y @mozilla/firefox-devtools-mcp@latest \
    --firefox-path "${FIREFOX_MCP_BIN}" \
    --profile-path "${FIREFOX_MCP_PROFILE}"
```

For a headless configuration, the option `--headless` or `--env "FIREFOX_HEADLESS=true"` can be used, or a separate registration can be made:

```Bash
$CODEX_BIN mcp add firefox-devtools-headless \
    --env "DISPLAY=${DISPLAY}" \
    --env "WAYLAND_DISPLAY=${WAYLAND_DISPLAY}" \
    --env "XDG_RUNTIME_DIR=${XDG_RUNTIME_DIR}" \
    -- \
    npx -y @mozilla/firefox-devtools-mcp@latest \
    --firefox-path "${FIREFOX_MCP_BIN}" \
    --profile-path "${FIREFOX_MCP_PROFILE}" \
    --headless \
    --viewport 1860x1020
```

```Bash
$CODEX_BIN
```

```prompt
Please open Firefox via MCP, go to startpage.com, search for the weather in São Paulo and then report very briefly what the weather is this week.
```

```prompt
Using the Firefox DevTools MCP, please launch Firefox with `headless: true`. Make the initial browser calls sequentially. Before browsing, call `get_firefox_info` and confirm it reports `Headless: Yes`. If it does not, stop and report the failure. Then visit DuckDuckGo, search for São Paulo’s weather this week, and summarise the results.
```

The MCP registrations can be removed in ways like the following:

```Bash
"${CODEX_BIN}" mcp remove firefox-devtools
"${CODEX_BIN}" mcp remove firefox-devtools-headless
```
