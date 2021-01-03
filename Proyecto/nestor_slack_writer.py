from slack import WebClient
#from nestorbot import NestorBot
import os
from pathlib import Path
from dotenv import load_dotenv
import pika

#Conexión a slack
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola 'hello'
    channel.queue_declare(queue='writer')


    #Recibir mensajes de la cola es más complejo. Funciona suscribiendo una función de devolución de llamada ("callback"). Cada vez que recibimos un mensaje, esta función "callback" es llamada por la libreria Pika. En nuestro caso, esta función imprimirá en la pantalla el contenido del mensaje.
    def callback(ch, method, properties, body):
        slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))
        slack_web_client.chat_postMessage(channel='#general',text=message)

    channel.basic_consume(queue='writer', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)