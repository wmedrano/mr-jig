import pytest
import main
import quart


@pytest.fixture()
def app() -> quart.Quart:
    main.app.testing = True
    return main.app


@pytest.fixture()
def client(app: quart.Quart) -> quart.typing.TestClientProtocol:
    return app.test_client()


@pytest.mark.asyncio
async def test_homepage(client: quart.typing.TestClientProtocol):
    response = await client.get('/')
    assert response.status_code == 200
    assert len(await response.data) > 0
