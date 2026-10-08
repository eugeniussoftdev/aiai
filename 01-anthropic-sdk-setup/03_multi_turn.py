"""Multi-turn conversation: pass prior user/assistant turns in `messages`.

Docs:
  https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages#multiple-conversational-turns
"""

from cca_common import MODEL, get_client

client = get_client()

message = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Can you describe LLMs to me in two sentences?"},
    ],
)

print(f"stop_reason: {message.stop_reason}")
for block in message.content:
    if block.type == "text":
        print(block.text)
