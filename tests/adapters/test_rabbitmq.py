import json

from unittest.mock import patch


@patch("adapters.rabbitmq.pika")
def test_mq_session_enter(pika_mock, rabbitmq_session):
    result = rabbitmq_session.__enter__()
    pika_mock.PlainCredentials.assert_called_with("test", "test")
    pika_mock.ConnectionParameters.assert_called_with(
        host="localhost",
        port=5672,
        credentials=pika_mock.PlainCredentials.return_value,
        virtual_host="/",
    )
    pika_mock.BlockingConnection(pika_mock.ConnectionParameters.return_value)
    assert result == pika_mock.BlockingConnection.return_value


@patch("adapters.rabbitmq.pika")
def test_mq_session_exit(pika_mock, rabbitmq_session):
    rabbitmq_session.__enter__()
    rabbitmq_session.__exit__("type", "value", "tb")
    pika_mock.BlockingConnection.return_value.close.assert_called()


def test_rabbitmq_adapter_get_session(rabbitmq_adapter):
    session = rabbitmq_adapter.get_session()
    assert session.host == "localhost"
    assert session.port == 5672
    assert session.username == "test"
    assert session.password == "test"
    assert session.virtual_host == "/"


def test_rabbitmq_adapter_send_message(rabbitmq_adapter):
    message = {"test": "test"}
    with patch(
        'adapters.rabbitmq.RabbitMQAMQPAdapter.get_session'
    ) as wrapped_adapter:
        rabbitmq_adapter.send_message(message)
        channel_mock = wrapped_adapter.return_value.__enter__.return_value.channel
        channel_mock.assert_called()
        channel_mock.return_value.exchange_declare.assert_called_with(
            exchange="rabbitmq",
            exchange_type="topic",
        )
        channel_mock.return_value.basic_publish.assert_called_with(
            exchange="rabbitmq",
            routing_key=rabbitmq_adapter.topic,
            body=json.dumps(message),
        )


def test_rabbitmq_adapter_receive_messages(rabbitmq_adapter):
    with patch(
        'adapters.rabbitmq.RabbitMQAMQPAdapter.get_session'
    ) as wrapped_adapter:
        rabbitmq_adapter.receive_messages()
        channel_mock = wrapped_adapter.return_value.__enter__.return_value.channel
        channel_mock.assert_called()
        channel_mock.return_value.exchange_declare.assert_called_with(
            exchange="rabbitmq",
            exchange_type="topic",
        )
        channel_mock.return_value.queue_declare.assert_called_with(
            "",
            exclusive=True,
        )
        channel_mock.return_value.queue_bind.assert_called_with(
            exchange="rabbitmq",
            queue=channel_mock.return_value.queue_declare.return_value.method.queue,
            routing_key=rabbitmq_adapter.topic,
        )
        channel_mock.return_value.basic_consume.assert_called_with(
            queue=channel_mock.return_value.queue_declare.return_value.method.queue,
            on_message_callback=rabbitmq_adapter.callback,
            auto_ack=True,
        )
        channel_mock.return_value.start_consuming.assert_called()
