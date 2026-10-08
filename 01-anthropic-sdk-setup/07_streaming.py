"""Streaming Messages: print tokens as they arrive.

Docs:
  https://docs.anthropic.com/en/api/messages-streaming
  https://platform.claude.com/docs/en/api/sdks/python
"""

from cca_common import MODEL, get_client

client = get_client()

with client.messages.stream(
    model=MODEL,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "Count from 1 to 5, one number per line.",
        }
    ],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    print()

final = stream.get_final_message()
print(f"\nstop_reason: {final.stop_reason}")
print(f"usage: input={final.usage.input_tokens} output={final.usage.output_tokens}")
