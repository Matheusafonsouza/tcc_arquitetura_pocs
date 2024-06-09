import json

from adapters.rabbitmq import RabbitMQAMQPAdapter
from domain.service import log


def callback(channel, method, properties, body):
    message = json.loads(body.decode("utf-8"))
    print("INFO -> ", message)
    log(message)


def main():
    RabbitMQAMQPAdapter(
        host="rabbitmq",
        port=5672,
        username="test",
        password="test",
        virtual_host="/",
        topic="test",
        callback=callback,
    ).receive_messages()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
