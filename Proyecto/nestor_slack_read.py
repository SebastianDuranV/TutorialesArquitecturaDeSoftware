from slack import WebClient
#from nestorbot import NestorBot
import os
from pathlib import Path
from dotenv import load_dotenv
import pika

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._choose_message(),
            ],
        }

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola 'hello'
    channel.queue_declare(queue='read')

    message = nestor_bot.get_message_payload()
    if message:
        channel.basic_publish(exchange='',
                        routing_key='read',
                        body=message)


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