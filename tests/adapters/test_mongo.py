import pytest
from bson import ObjectId
from adapters.database.nosql.mongo import MongoDatabase

@pytest.fixture
def setup_data():
  users_collection = MongoDatabase("mongodb://root:example@localhost:27017/", "test_database", "users")
  test_user = {
  "_id": ObjectId("65f0c9c3663a7973659789e7"),
  "name": "test",
  "email":
  "test@example.com"
  }
  return users_collection, test_user

def test_mongo_create(setup_data):
  users_collection, test_user = setup_data
  result = users_collection.create(test_user)
  assert result["name"] == "test"
  assert result["email"] == "test@example.com"

def test_mongo_get(setup_data):
  users_collection, test_user = setup_data
  result = users_collection.get(str(test_user["_id"]))
  assert result["name"] == test_user["name"]

def test_mongo_update(setup_data):
  users_collection, test_user = setup_data
  result = users_collection.update(str(test_user["_id"]), {"name": "test1"})
  assert result["name"] == "test1"
  assert result["email"] == test_user["email"]

def test_mongo_delete(setup_data):
  users_collection, test_user = setup_data
  users_collection.delete(str(test_user["_id"]))
  result = users_collection.get(str(test_user["_id"]))
  assert result is None
