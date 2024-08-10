import pytest
from bson import ObjectId


@pytest.fixture
def test_user():
  return {
    "_id": ObjectId("65f0c9c3663a7973659789e7"),
    "name": "test",
    "email":
    "test@example.com"
  }


def test_mongo_create(test_user, mongo_database):
  result = mongo_database.create(test_user)
  assert result["name"] == "test"
  assert result["email"] == "test@example.com"


def test_mongo_get(test_user, mongo_database):
  result = mongo_database.get(str(test_user["_id"]))
  assert result["name"] == test_user["name"]


def test_mongo_update(test_user, mongo_database):
  result = mongo_database.update(str(test_user["_id"]), {"name": "test1"})
  assert result["name"] == "test1"
  assert result["email"] == test_user["email"]


def test_mongo_delete(test_user, mongo_database):
  mongo_database.delete(str(test_user["_id"]))
  result = mongo_database.get(str(test_user["_id"]))
  assert result is None
