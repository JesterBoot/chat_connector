import pytest

from utils import get_token


@pytest.mark.asyncio
async def test_get_token(token_map):
    token = await get_token("ChatTransportDiscord", token_map)
    assert token == "discord_token_value"

    with pytest.raises(ValueError):
        await get_token("NonExistentTransport", token_map)
