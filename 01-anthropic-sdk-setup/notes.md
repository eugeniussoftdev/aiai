# Notes — `stop_reason`

Every Messages API response includes `stop_reason`: why Claude stopped generating. It is a normal completion signal, not an error.

Docs: [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)

| Value | When it occurs | What to do |
| --- | --- | --- |
| `end_turn` | Claude finished naturally | Use the response |
| `max_tokens` | Hit your `max_tokens` limit | Raise `max_tokens` or continue |
| `stop_sequence` | Hit one of your `stop_sequences` | Check `stop_sequence` for which one |
| `tool_use` | Claude is calling a client tool | Run the tool, return `tool_result`, call again |
| `pause_turn` | Server-tool loop hit iteration limit | Send assistant content back to continue |
| `refusal` | Claude declined to respond | Read details / retry on a fallback model |
| `model_context_window_exceeded` | Response filled the context window | Treat as truncated |

For a simple chat reply you will usually see `end_turn`. Agentic loops typically continue while `stop_reason == "tool_use"`.

Related: [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
