"""Minimal Messages API call.

Docs:
  https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages#basic-request-and-response
  https://docs.anthropic.com/en/api/messages
  https://platform.claude.com/docs/en/api/sdks/python
"""

from cca_common import MODEL, get_client

client = get_client()

message = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(message)
for block in message.content:
    if block.type == "text":
        print(block.text)
