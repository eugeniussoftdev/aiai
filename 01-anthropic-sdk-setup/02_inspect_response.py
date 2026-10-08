"""Inspect Message fields: content, stop_reason, usage, stop_sequence.

Docs:
  https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
  https://docs.anthropic.com/en/api/messages
"""

from cca_common import MODEL, get_client

client = get_client()

message = client.messages.create(
    model=MODEL,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "Reply with one short sentence explaining what a stop_reason is.",
        }
    ],
)

print(f"id:            {message.id}")
print(f"model:         {message.model}")
print(f"role:          {message.role}")
print(f"stop_reason:   {message.stop_reason}")
print(f"stop_sequence: {message.stop_sequence}")
print(f"usage:         input={message.usage.input_tokens} output={message.usage.output_tokens}")
print("--- content ---")
for block in message.content:
    print(f"[{block.type}] {getattr(block, 'text', block)}")
