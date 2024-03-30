import pytest

from tests.conftest import MockChatTransportWithErrors


@pytest.mark.asyncio
async def test_chat_transport_abstract_methods(faker):
    chat_id = faker.random_number(digits=9)
    message = faker.text()
    transport = MockChatTransportWithErrors("mock_token")

    with pytest.raises(NotImplementedError):
        await transport.add_handler("event", lambda x: x)

    with pytest.raises(NotImplementedError):
        await transport.send_message(chat_id, message)

    with pytest.raises(NotImplementedError):
        await transport.run()
