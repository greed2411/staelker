
import pika
import json

import os

import logging
logging.getLogger().setLevel(logging.INFO)


import dotenv
dotenv.load_dotenv()

RMQ_USERNAME = os.getenv("RMQ_USERNAME")
RMQ_PWD = os.getenv("RMQ_PWD")
RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PORT = os.getenv("RMQ_PORT")

rmq_url = f"amqp://{RMQ_USERNAME}:{RMQ_PWD}@{RMQ_HOST}:{RMQ_PORT}/%2F"
print(f"consuming at {rmq_url}")
parameters = pika.URLParameters(rmq_url)

import time
print("consumer sleeping and waiting for rmq")
time.sleep(10)

def on_message_callback(ch, method, properties, body):
    print(body)


def main():

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_consume(queue='stream', auto_ack=True, on_message_callback=on_message_callback)
    channel.start_consuming()


if __name__ == "__main__":

    main()