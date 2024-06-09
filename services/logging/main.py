import json

from adapters.rabbitmq import RabbitMQAMQPAdapter
from ports.amqp import AMQPPort
from domain.service import log


class Worker:
    def __init__(self, adapter: AMQPPort):
        self.adapter = adapter

    def handle_message(self):
        self.adapter.receive_messages()


def callback(channel, method, properties, body):
    message = json.loads(body.decode("utf-8"))
    print("INFO -> ", message)
    log(message)


def main():
    Worker(
        adapter=RabbitMQAMQPAdapter(
            host="rabbitmq",
            port=5672,
            username="test",
            password="test",
            virtual_host="/",
            topic="test",
            callback=callback,
        )
    ).handle_message()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
