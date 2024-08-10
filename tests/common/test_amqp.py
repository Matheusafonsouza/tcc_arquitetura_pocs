from common.amqp import get_rabbitmq_adapter
from adapters.rabbitmq import RabbitMQAMQPAdapter


def test_get_rabbitmq_adapter():
    adapter = get_rabbitmq_adapter()
    assert adapter.host == 'rabbitmq'
    assert adapter.port == 5672
    assert adapter.username == 'guest'
    assert adapter.password == 'guest'
    assert adapter.virtual_host == '/'
    assert adapter.topic == 'test'
    assert adapter.callback == None
