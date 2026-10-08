"""Async Messages API with AsyncAnthropic.

Docs:
  https://platform.claude.com/docs/en/api/sdks/python
"""

import asyncio

from cca_common import MODEL, get_async_client


async def main() -> None:
    client = get_async_client()
    message = await client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": "Say hello asynchronously in one sentence."}],
    )
    print(f"stop_reason: {message.stop_reason}")
    for block in message.content:
        if block.type == "text":
            print(block.text)


if __name__ == "__main__":
    asyncio.run(main())
