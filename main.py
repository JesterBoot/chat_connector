import asyncio

import settings
from setup import initialize_bot, start_bot

logger = settings.logger


async def main():
    transport = await initialize_bot()
    await start_bot(transport)


if __name__ == "__main__":
    asyncio.run(main())
