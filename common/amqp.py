from adapters.rabbitmq import RabbitMQAMQPAdapter


def get_rabbitmq_adapter(callback = None) -> RabbitMQAMQPAdapter:
    return RabbitMQAMQPAdapter(
        host="rabbitmq",
        port=5672,
        username="guest",
        password="guest",
        virtual_host="/",
        topic="test",
        callback=callback,
    )
