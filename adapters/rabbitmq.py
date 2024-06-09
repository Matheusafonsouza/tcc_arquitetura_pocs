import json

import pika
from pika.adapters.blocking_connection import BlockingConnection

from ports.amqp import AMQPPort


class MQSession:
    def __init__(self, host, port, username, password, virtual_host):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.virtual_host = virtual_host

    def __enter__(self) -> BlockingConnection:
        credentials = pika.PlainCredentials(self.username, self.password)
        params = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=credentials,
            virtual_host=self.virtual_host)
        self.connection = pika.BlockingConnection(params)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.close()


class RabbitMQAMQPAdapter(AMQPPort):
    def __init__(self, host, port, username, password, virtual_host, topic, callback = None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.virtual_host = virtual_host
        self.topic = topic
        self.callback = callback

    def get_session(self):
        return MQSession(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            virtual_host=self.virtual_host,
        )
        
    def send_message(self, message: dict):
        with self.get_session() as session:
            channel = session.channel()
            channel.exchange_declare(
                exchange="rabbitmq", exchange_type="topic")
            channel.basic_publish(
                exchange="rabbitmq",
                routing_key=self.topic,
                body=json.dumps(message),
            )

    def receive_messages(self):
        with self.get_session() as session:
            channel = session.channel()
            channel.exchange_declare(
                exchange="rabbitmq", exchange_type="topic")
            result = channel.queue_declare("", exclusive=True)
            queue = result.method.queue
            channel.queue_bind(
                exchange="rabbitmq", queue=queue, routing_key=self.topic)
            channel.basic_consume(
                queue=queue,
                on_message_callback=self.callback,
                auto_ack=True)
            channel.start_consuming()