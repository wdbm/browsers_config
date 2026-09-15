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

```Bash
$CODEX_BIN
```

```prompt
Please open Firefox via MCP, go to startpage.com, search for the weather in São Paulo and then report very briefly what the weather is this week.
```
