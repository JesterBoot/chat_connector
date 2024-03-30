import typing
from abc import ABC, abstractmethod

import discord
from aiogram import Bot, Dispatcher, types
from discord.ext import commands


class ChatTransport(ABC):
    def __init__(self, token: str):
        self.token: str = token

    @abstractmethod
    async def add_handler(self, event: str, handler):
        raise NotImplementedError

    @abstractmethod
    async def send_message(self, chat_id: int | str, msg: str):
        raise NotImplementedError("Subclasses must implement send_message")

    @abstractmethod
    async def run(self):
        raise NotImplementedError("Subclasses must implement run")


class ChatTransportDiscord(ChatTransport):
    def __init__(self, token: str):
        super().__init__(token)
        self.bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

    async def add_handler(self, event: str, handler: typing.Callable):
        async def on_message(message: discord.Message):
            if message.author == self.bot.user:
                return
            await handler(message.channel.id, message.content)

        self.bot.event(on_message)

    async def send_message(self, chat_id: int | str, msg: str):
        channel = self.bot.get_channel(chat_id)  # type: ignore
        if channel:
            await channel.send(msg)  # type: ignore

    async def run(self):
        await self.bot.start(self.token)


class ChatTransportTelegram(ChatTransport):
    def __init__(self, token: str):
        super().__init__(token)
        self.bot: Bot = Bot(token=token)
        self.dp: Dispatcher = Dispatcher()

    async def add_handler(self, event: str, handler):
        @self.dp.message()
        async def handle_message(message: types.Message):
            await handler(message.chat.id, message.text)

    async def send_message(self, chat_id: int | str, msg: str):
        await self.bot.send_message(chat_id, msg)

    async def run(self):
        await self.dp.start_polling(self.bot)
