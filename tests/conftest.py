import pytest
import mongomock

@pytest.fixture()
@mongomock.patch()
def mongo_db():
    return mongomock.MongoClient().collection
