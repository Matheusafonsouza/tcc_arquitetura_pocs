import json

from common.common_service import (
    ping,
    ping_server,
    get_user,
    create_user,
    delete_user,
    update_user,
)
from adapters.rabbitmq import RabbitMQAMQPAdapter
from unittest.mock import MagicMock


def test_ping():
    assert ping() == { "ping": True }


def test_ping_server():
    http_adapter_mock = MagicMock()
    amqp_adapter_mock = MagicMock()

    server_url = "http://test.com"
    response_content = { "ok": True }
    response_mock = {
        "status_code": 200,
        "content": response_content,
    }
    http_adapter_mock.return_value.get.return_value = response_mock

    response = ping_server(
        http_adapter=http_adapter_mock,
        amqp_adapter=amqp_adapter_mock,
        server_url=server_url,
        route="/test"
    )

    assert response.status_code == 200
    assert json.loads(response.body.decode()) == response_content
    http_adapter_mock.assert_called_with(server_url)
    http_adapter_mock.return_value.get.assert_called_with("/test")
    amqp_adapter_mock.send_message.assert_called_with(response_mock)


def test_get_user(postgres_database):
    created_user = postgres_database.create({"name": "test"})
    user = get_user(created_user.get("id"), postgres_database)
    assert user.get("id") == created_user.get("id")
    assert user.get("name") == created_user.get("name")


def test_create_user(postgres_database):
    user = create_user({"name": "test"}, postgres_database)
    assert user.get("id")
    assert user.get("name") == "test"


def testdelete_user(postgres_database):
    created_user = postgres_database.create({"name": "test"})
    delete_user(created_user.get("id"), postgres_database)
    assert get_user(created_user.get("id"), postgres_database) is None


def test_update_user(postgres_database):
    created_user = postgres_database.create({"name": "test"})
    update_user(created_user.get("id"), {"name": "test2"}, postgres_database)
    updated_user = get_user(created_user.get("id"), postgres_database)
    assert created_user.get("id") == updated_user.get("id")
    assert created_user.get("name") != updated_user.get("name")
    assert updated_user.get("name") == "test2"
