import json
import sys
from ports.amqp import AMQPPort
from common.database import get_mongo_database
from common.amqp import get_rabbitmq_adapter
from domain.repositories.log_repository import LogRepository


log_repository = LogRepository(
    adapter=get_mongo_database("logs")
)


def callback(channel, method, properties, body):
    message = json.loads(body.decode("utf-8"))
    print("INFO -> ", message)
    log_repository.create(({"message": message}))


class Worker:
    def __init__(self, adapter: AMQPPort):
        self.adapter = adapter

    def handle_message(self):
        self.adapter.receive_messages()


def main():
    Worker(
        adapter=get_rabbitmq_adapter(callback),
    ).handle_message()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
