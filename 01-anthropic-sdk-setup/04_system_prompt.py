"""System prompt via top-level `system` (there is no system role in messages).

Docs:
  https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages
  https://docs.anthropic.com/en/api/messages
"""

from cca_common import MODEL, get_client

client = get_client()

message = client.messages.create(
    model=MODEL,
    max_tokens=256,
    system="You are a concise CCA-F study coach. Prefer short, exam-ready answers.",
    messages=[
        {
            "role": "user",
            "content": "What is the Messages API in one sentence?",
        }
    ],
)

print(f"stop_reason: {message.stop_reason}")
for block in message.content:
    if block.type == "text":
        print(block.text)
