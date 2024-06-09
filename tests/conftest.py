import pytest

from adapters.rabbitmq import RabbitMQAMQPAdapter, MQSession
from adapters.database.sql.postgres import PostgresDatabase


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
    )
