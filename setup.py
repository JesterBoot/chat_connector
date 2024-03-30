import settings
from business_logic import SimpleBusinessLogicBot
from chat_transport import ChatTransportDiscord, ChatTransportTelegram
from mappings import TOKEN_MAP
from utils import get_token


async def initialize_bot():
    bot_type = settings.CONFIG.get("bot_type")

    if bot_type == "discord":
        transport_cls = ChatTransportDiscord
    elif bot_type == "telegram":
        transport_cls = ChatTransportTelegram
    else:
        raise ValueError("Invalid bot type specified in config")

    token = await get_token(name=transport_cls.__name__, token_map=TOKEN_MAP)
    transport = transport_cls(token)
    logic = SimpleBusinessLogicBot(transport)
    await transport.add_handler("message", logic.handle_message)

    settings.logger.info(f"Starting {transport_cls.__name__}")

    return transport


async def start_bot(transport):
    try:
        await transport.run()
    except Exception as e:
        settings.logger.error(f"Error running transport: {e}")
        raise
    finally:
        settings.logger.info(f"Finished running {type(transport).__name__}")
