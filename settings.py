import logging
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.INFO)


CONFIG = {
    "discord_token": str(os.getenv("DS_TOKEN")),
    "telegram_token": str(os.getenv("TG_TOKEN")),
    "bot_type": str(os.getenv("BOT_TYPE")),
}
