# 03 — Agentic Loop Foundations

## Concept: Tools (tool use)

Messages = talk. Tools = Claude can **ask your app to do something** (DB query, 3rd-party API, calendar, etc.), then use the result to continue.

Flow:
1. You send a user message **plus** tool definitions (name, description, input schema).
2. Claude replies with `stop_reason: tool_use` and which tool + arguments.
3. **Your code** runs the tool (Claude does not call your DB/API by itself for client tools).
4. You send a `tool_result` back in the conversation.
5. Claude answers the user — or requests another tool.

Examples of tools: `get_weather(city)`, `query_orders(user_id)`, `get_calendar_events(date)`.

## Practice

### TODO 1 — Tools + one loop turn

- [ ] Define one simple tool (e.g. fake `get_weather` that returns hardcoded JSON — no real API yet)
- [ ] Call `messages.create` with `tools=[...]` and a user question that needs it
- [ ] Print `stop_reason` and any `tool_use` content blocks (name + input)
- [ ] Execute the tool in Python and send a `tool_result` message back
- [ ] Confirm the final reply has `stop_reason: end_turn` and uses the tool data
- [ ] Sketch 3 tools you might need for a real app (name + one-line purpose only)

### TODO 2 — Growing `messages` / context (dig deeper later)

Related to the agentic loop: each `messages.create` resends the full history, so a long loop makes the array (and cost/latency) blow up, and can hit the context window.

- [ ] Watch `messages` length / `usage.input_tokens` across loop iterations
- [ ] Add a max-iterations guard (e.g. stop after N tool rounds)
- [ ] Read about trim / summarize (compaction) and when you’d drop old turns
- [ ] Practice returning small tool results (key fields only), not huge payloads
- [ ] Skim prompt caching as a way to reuse a stable prefix more cheaply
- [ ] Note: full session/context design also lives in `06-session-context-state/` — revisit there to master

### TODO 3 — MCP (create a tiny server, connect later)

MCP = standard way to **host and share tools** for AI agents (like a shared integration service, not a FE API gateway).

**Where to store it**
- Separate process / folder from your chat script (e.g. `mcp_servers/order_tools/server.py`)
- Owns DB/API code (Postgres, Shippo, Stripe…)
- Agent apps only **connect** to it — they don’t copy tool implementations
- Local: usually `stdio` (client starts the server process)
- Shared/remote: `http` transport so many agents can hit one URL

**Minimal server (FastMCP)** — prefer `from fastmcp import FastMCP` (standalone). Older code uses `from mcp.server.fastmcp import FastMCP`.

```python
# mcp_servers/order_tools/server.py
from fastmcp import FastMCP

mcp = FastMCP("order-tools")

@mcp.tool
def lookup_order(order_id: str) -> dict:
    """Fake Postgres lookup for practice."""
    return {"order_id": order_id, "status": "shipped", "city": "Lisbon"}

@mcp.tool
def get_shipment(tracking_id: str) -> dict:
    """Fake Shippo tracking for practice."""
    return {"tracking_id": tracking_id, "eta": "2026-10-12"}

if __name__ == "__main__":
    mcp.run()  # default stdio — Claude Code / MCP client spawns this file
    # mcp.run(transport="http", port=8000)  # optional: share over HTTP
```

Install when you practice: `uv add fastmcp` (or `pip install fastmcp`).

- [ ] Create `mcp_servers/order_tools/server.py` with 1–2 fake tools (hardcoded returns)
- [ ] Run it once / inspect with FastMCP or MCP inspector so tools show up
- [ ] Sketch how a second app would reuse the same server (no copy of Postgres code)
- [ ] Note in one sentence: hardcoded `tools=[...]` in Messages API vs tools from MCP
- [ ] Wire a client later (Claude Code MCP config or Agent SDK) — mastery pass

## Docs

- [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
- [Stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)
- [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [MCP intro](https://modelcontextprotocol.io/introduction)
- [FastMCP quickstart](https://gofastmcp.com/getting-started/quickstart)
