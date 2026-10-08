"""Vision: send an image content block with a local PNG.

Docs:
  https://docs.anthropic.com/en/docs/build-with-claude/working-with-messages#vision
  https://docs.anthropic.com/en/docs/build-with-claude/vision
"""

import base64
from pathlib import Path

from cca_common import MODEL, get_client

IMAGE_PATH = Path(__file__).parent / "assets" / "sample.png"

client = get_client()
image_data = base64.standard_b64encode(IMAGE_PATH.read_bytes()).decode("utf-8")

message = client.messages.create(
    model=MODEL,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe this image in one short sentence.",
                },
            ],
        }
    ],
)

print(f"stop_reason: {message.stop_reason}")
for block in message.content:
    if block.type == "text":
        print(block.text)
