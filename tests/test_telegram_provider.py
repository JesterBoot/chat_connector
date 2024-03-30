from unittest.mock import AsyncMock

import pytest


@pytest.mark.asyncio
async def test_telegram_add_handler(telegram_transport):
    async def dummy_handler():
        pass

    await telegram_transport.add_handler("message", dummy_handler)


@pytest.mark.asyncio
async def test_telegram_send_message(telegram_transport, faker):
    chat_id = faker.random_number(digits=9)
    message = faker.text()
    await telegram_transport.send_message(chat_id, message)


async def test_telegram_run(telegram_transport):
    await telegram_transport.run()

    telegram_transport.bot.start_polling.assert_called_once()
    telegram_transport.assert_awaited_once_with(telegram_transport.token)


@pytest.mark.asyncio
async def test_telegram_transport_error_handling(telegram_transport):
    mocked_start = AsyncMock(side_effect=Exception("Test error occurred"))
    telegram_transport.bot.start = mocked_start

    with pytest.raises(Exception):
        await telegram_transport.run()
