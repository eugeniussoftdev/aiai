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

## Practice (TODO)

- [ ] Define one simple tool (e.g. fake `get_weather` that returns hardcoded JSON — no real API yet)
- [ ] Call `messages.create` with `tools=[...]` and a user question that needs it
- [ ] Print `stop_reason` and any `tool_use` content blocks (name + input)
- [ ] Execute the tool in Python and send a `tool_result` message back
- [ ] Confirm the final reply has `stop_reason: end_turn` and uses the tool data
- [ ] Sketch 3 tools you might need for a real app (name + one-line purpose only)

## Docs

- [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
- [Stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
