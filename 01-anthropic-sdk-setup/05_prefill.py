"""Prefill Claude's response by ending `messages` with an assistant turn.

Docs:
  https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages#prefilling-claudes-response
"""

from cca_common import MODEL, get_client

client = get_client()

message = client.messages.create(
    model=MODEL,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "Write a haiku about the Anthropic Messages API.",
        },
        {
            "role": "assistant",
            "content": "Here is a haiku:\n\n",
        },
    ],
)

print(f"stop_reason: {message.stop_reason}")
# Prefill is not echoed back; print it so you see the full intended reply.
print("Here is a haiku:\n")
for block in message.content:
    if block.type == "text":
        print(block.text)
