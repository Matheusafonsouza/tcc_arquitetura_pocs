import os
import json

from common.database import (
    get_postgres_database,
    get_mongo_database,
)
from adapters.rabbitmq import RabbitMQAMQPAdapter
from unittest.mock import MagicMock, patch
from adapters.database.sql.postgres import User

@patch.dict(os.environ, {
    "PG_USER": "root",
    "PG_PASS": "root",
    "PG_HOST": "localhost",
    "PG_PORT": "5432",
    "PG_DB": "database",
}, clear=True)
def test_get_postgres_database():
    adapter = get_postgres_database("users", "test")
    assert adapter.get_table("users") == User


@patch.dict(os.environ, {
    "MONGO_USER": "root",
    "MONGO_PASS": "example",
    "MONGO_HOST": "localhost",
    "MONGO_PORT": "27017",
}, clear=True)
def test_get_mongo_database():
    adapter = get_mongo_database("test_database", "users")
    user = adapter.create({ "name": "name" })
    assert user.get("name") == "name"
