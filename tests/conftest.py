import pytest
import mongomock
from app import create_app
from flask import Flask
from typing import Generator, Any


@pytest.fixture()
@mongomock.patch()
def mongo_db():
    return mongomock.MongoClient().collection


@pytest.fixture()
def app() -> Generator[Flask, Any, Any]:
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
