import pytest
import main
from flask.testing import Flask, FlaskClient


@pytest.fixture()
def app() -> Flask:
    app = main.app
    app.config.update({'TESTING': True})
    return app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_homepage(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data is not None
