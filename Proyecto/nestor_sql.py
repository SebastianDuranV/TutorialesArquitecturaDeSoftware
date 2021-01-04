from nestor_bot import NestorBot
import pika
import os
import sys

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='writer')


    def callback(ch, method, properties, body):
        print(body)
        #return consultaSql(body)

    channel.basic_consume(queue='writer', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

    if answer != -1:
        channel.basic_publish(exchange='',
                        routing_key='write',
                        body=answer)


# Bucle
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            connection.close()
            sys.exit(0)
        except SystemExit:
            connection.close()
            os._exit(0)