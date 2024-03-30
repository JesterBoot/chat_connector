from chat_transport import ChatTransport


class SimpleBusinessLogicBot:
    def __init__(self, transport: ChatTransport):
        self.transport = transport

    async def handle_message(self, chat_id: int | str, msg: str):
        response = f"Hi! Your message was received: {msg}"
        await self.transport.send_message(chat_id, response)
