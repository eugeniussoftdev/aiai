# aiai — CCA-F Learning Path

Personal study repo for **Claude Certified Architect – Foundations (CCA-F)**.

## Setup

1. Install [uv](https://docs.astral.sh/uv/) if needed.
2. From the repo root:

```bash
uv sync
cp .env.example .env
# Put your key in .env — https://console.anthropic.com/
```

3. Run a lesson script:

```bash
uv run python 01-anthropic-sdk-setup/01_basic_message.py
```

## Learning path

| Folder | Topic |
| --- | --- |
| [01-anthropic-sdk-setup](01-anthropic-sdk-setup/) | Anthropic SDK Setup |
| [02-agent-sdk-setup](02-agent-sdk-setup/) | Agent SDK Setup |
| [03-agentic-loop-foundations](03-agentic-loop-foundations/) | Agentic Loop Foundations |
| [04-orchestration-multi-agent](04-orchestration-multi-agent/) | Orchestration & Multi-Agent Architecture |
| [05-advanced-agent-patterns](05-advanced-agent-patterns/) | Advanced Agent Patterns & Execution Control |
| [06-session-context-state](06-session-context-state/) | Session Management, Context & State |
| [07-claude-code-config-safety](07-claude-code-config-safety/) | Claude Code Configuration, Permissions & Safety |
| [08-reliability-output-validation](08-reliability-output-validation/) | Reliability & Output Validation |

## Docs

- [Working with Messages](https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages)
- [Messages API reference](https://docs.anthropic.com/en/api/messages)
- [Stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [Python SDK](https://platform.claude.com/docs/en/api/sdks/python)
- [Streaming Messages](https://docs.anthropic.com/en/api/messages-streaming)
- [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)
- [Get an API key](https://console.anthropic.com/)
