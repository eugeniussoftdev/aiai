# 01 — Anthropic SDK Setup

ExamPro lab: **Anthropic SDK Setup**.

Runnable Messages API examples from Anthropic’s [Working with Messages](https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages) guide, plus stop-reason inspection, streaming, and async.

## Prerequisites

From the repo root:

```bash
uv sync
cp .env.example .env   # add ANTHROPIC_API_KEY
```

Get a key: [console.anthropic.com](https://console.anthropic.com/)

## Scripts

| Script | Topic |
| --- | --- |
| `01_basic_message.py` | Minimal `messages.create` |
| `02_inspect_response.py` | `content`, `stop_reason`, `usage` |
| `03_multi_turn.py` | Multi-turn history |
| `04_system_prompt.py` | Top-level `system` prompt |
| `05_prefill.py` | Prefill assistant response |
| `06_vision.py` | Image content block |
| `07_streaming.py` | Streaming responses |
| `08_async.py` | `AsyncAnthropic` |

```bash
uv run python 01-anthropic-sdk-setup/01_basic_message.py
```

See [notes.md](notes.md) for the `stop_reason` cheat sheet.

## Docs

- [Working with Messages](https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages)
- [Messages API reference](https://docs.anthropic.com/en/api/messages)
- [Stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)
- [Python SDK](https://platform.claude.com/docs/en/api/sdks/python)
- [Streaming Messages](https://docs.anthropic.com/en/api/messages-streaming)
- [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)
- [ExamPro CCA-F](https://www.exampro.co/cca-f)
