import pytest
import mongomock
from app import create_app
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
from typing import Generator, Any


@pytest.fixture()
@mongomock.patch()
def mongo_db():
    """Fixture to set up a test database."""
    return mongomock.MongoClient().collection


@pytest.fixture()
def app() -> Generator[Flask, Any, Any]:
    """Fixture to set up a test app."""
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    """Fixture to set up a test client."""
    return app.test_client()


@pytest.fixture
def authenticated_client(client)-> FlaskClient:
    """Fixture to set up an authenticated client."""
    with client.session_transaction() as session:
        session["username"] = "test-user-1"
    return client


@pytest.fixture()
def runner(app: Flask) -> FlaskCliRunner:
    """Fixture to set up a test runner."""
    return app.test_cli_runner()
