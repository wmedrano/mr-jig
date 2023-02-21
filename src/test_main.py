import pytest
import main
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture()
def app() -> Flask:
    return main.app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_homepage(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data is not None
