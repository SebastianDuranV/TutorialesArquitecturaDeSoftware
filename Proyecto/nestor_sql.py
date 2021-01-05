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
    channel.queue_declare(queue='read')


    def callback(ch, method, properties, body):
        answer = body.decode().split(',')
        nestor = NestorBot(answer[0],answer[1])
        consult = nestor.get_message_payload(answer[2])
        print(consult)

        if consult != "OK ++":
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='writer')

            for i in consult:
                p = ""
                for j in i:
                    p += str(j) + ","
                channel.basic_publish(exchange='',routing_key='writer',body=p)

        #for i in answer:
        #    channel.basic_publish(exchange='',routing_key='writer',body=i)
        

    channel.basic_consume(queue='read', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

    #if answer != -1:
    #    channel.basic_publish(exchange='',
     #                   routing_key='write',
    #                    body=answer)


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