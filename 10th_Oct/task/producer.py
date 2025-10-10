# consumer.py
import pika
import json
import time

# 1. Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 2. create a queue(idempotent - creates only if not existing)
channel.queue_declare(queue="student_tasks")

#prepare a message
task = {
    "student_id": 101,
    "action": "generate_certificate",
    "email":"ygdybgfbt@yjfd.com"
}

# publish the message to queue
channel.basic_publish(
    exchange='',
    routing_key='student_tasks',
    body=json.dumps(task)
)

print("Task sent to queue")
connection.close()