import pytest

from adapters.rabbitmq import RabbitMQAMQPAdapter, MQSession
from adapters.database.sql.postgres import PostgresDatabase
from adapters.http import HTTPRequestAdapter
from adapters.database.nosql.mongo import MongoDatabase


@pytest.fixture
def rabbitmq_adapter():
    return RabbitMQAMQPAdapter(
        host="localhost",
        port=5672,
        username="test",
        password="test",
        virtual_host="/",
        topic="test",
    )


@pytest.fixture
def rabbitmq_session():
    return MQSession(
        host="localhost",
        port=5672,
        username="test",
        password="test",
        virtual_host="/",
    )


@pytest.fixture
def postgres_database():
    return PostgresDatabase(
        "postgresql://root:root@localhost:5432/database",
        "users",
        "test"
    )


@pytest.fixture
def mongo_database():
    return MongoDatabase(
        "mongodb://root:example@localhost:27017/",
        "test_database",
        "users"
    )


@pytest.fixture
def http_adapter():
    return HTTPRequestAdapter("https://jsonplaceholder.typicode.com")
