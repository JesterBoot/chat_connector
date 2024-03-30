from unittest.mock import AsyncMock

import pytest


@pytest.mark.asyncio
async def test_discord_add_handler(discord_transport):
    async def dummy_handler():
        pass

    await discord_transport.add_handler("message", dummy_handler)


@pytest.mark.asyncio
async def test_discord_send_message(discord_transport, faker):
    chat_id = faker.random_number(digits=9)
    message = faker.text()
    await discord_transport.send_message(chat_id, message)


@pytest.mark.asyncio
async def test_discord_run(discord_transport):
    mocked_start = AsyncMock()
    discord_transport.bot.start = mocked_start

    await discord_transport.run()

    mocked_start.assert_awaited_once_with(discord_transport.token)


@pytest.mark.asyncio
async def test_discord_transport_error_handling(discord_transport):
    mocked_start = AsyncMock(side_effect=Exception("Test error occurred"))
    discord_transport.bot.start = mocked_start

    with pytest.raises(Exception):
        await discord_transport.run()
