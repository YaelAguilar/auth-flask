from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)

RABBITMQ_URL = 'amqps://vumnphwp:04G37mBLNQfL_i6oM1cfMffWzwOOJifD@shrimp.rmq.cloudamqp.com/vumnphwp'
QUEUE_NAME = 'sensores'

@app.route('/sensor-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400
    if data ==1:
        data=100


    

    send_to_rabbitmq(data)
    return jsonify({"message": "Data received and sent to RabbitMQ"}), 200

def send_to_rabbitmq(data):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(data), properties=pika.BasicProperties(delivery_mode=2))
    connection.close()

if __name__ == '__main__':
    app.run(port=3001)
