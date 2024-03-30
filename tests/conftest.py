import typing
from unittest.mock import AsyncMock, patch

import pytest
from faker import Faker

from chat_transport import (ChatTransport, ChatTransportDiscord,
                            ChatTransportTelegram)


@pytest.fixture
def faker():
    return Faker()


@pytest.fixture
def token_map():
    return {
        "ChatTransportDiscord": "discord_token_value",
        "ChatTransportTelegram": "telegram_token_value",
    }


@pytest.fixture
def discord_transport(token_map):
    token = token_map.get("ChatTransportDiscord")
    return ChatTransportDiscord(token)


@pytest.fixture
def telegram_transport(token_map):
    token = token_map.get("ChatTransportTelegram")

    with patch("chat_transport.Bot") as MockBot:
        bot_instance = MockBot.return_value

        bot_instance.send_message = AsyncMock()
        bot_instance.start_polling = AsyncMock()

        return ChatTransportTelegram(token)


class MockChatTransportWithErrors(ChatTransport):
    async def add_handler(self, event: str, handler: typing.Callable):
        raise NotImplementedError("Subclasses must implement add_handler")

    async def send_message(self, chat_id: int | str, msg: str):
        raise NotImplementedError("Subclasses must implement send_message")

    async def run(self):
        raise NotImplementedError("Subclasses must implement run")
