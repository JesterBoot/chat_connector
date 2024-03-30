from typing import Optional


async def get_token(name: str, token_map: dict) -> str:
    token: Optional[str] = token_map.get(name)
    if not token:
        raise ValueError(
            f'Could not find the required environment variable for "{name}"'
        )
    return token
