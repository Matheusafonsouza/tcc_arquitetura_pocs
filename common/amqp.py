from adapters.rabbitmq import RabbitMQAMQPAdapter


def get_rabbitmq_adapter(callback = None) -> RabbitMQAMQPAdapter:
    return RabbitMQAMQPAdapter(
        host="rabbitmq",
        port=5672,
        username="test",
        password="test",
        virtual_host="/",
        topic="test",
        callback=callback,
    )
