from settings import CONFIG

TOKEN_MAP = {
    "ChatTransportDiscord": CONFIG.get("discord_token"),
    "ChatTransportTelegram": CONFIG.get("telegram_token"),
}
