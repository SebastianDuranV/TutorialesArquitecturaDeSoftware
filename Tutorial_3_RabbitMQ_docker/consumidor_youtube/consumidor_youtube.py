
from apiclient.discovery import build
import pika, sys, os

HOST = os.environ['RABBITMQ_HOST']

def main():

    api_key="AIzaSyDXLgOVJ-tvumVea3VH7af6wQI0WLAZYXs"
    youtube = build('youtube','v3', developerKey=api_key)

    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    #Nos aseguramos que existe una cola 'hello'
    channel.queue_declare(queue='hello')


    #Recibir mensajes de la cola es más complejo. Funciona suscribiendo una función de devolución de llamada ("callback"). Cada vez que recibimos un mensaje, esta función "callback" es llamada por la libreria Pika. En nuestro caso, esta función imprimirá en la pantalla el contenido del mensaje.
    def callback(ch, method, properties, body):
        req = youtube.search().list(q=body,part='snippet',type='video')
        res =req.execute()
        for i in res['items']:
            print("Titulo de video")
            print(i['snippet']['title'])
            print("Descripción")
            print(i['snippet']['description'])
            print()


    channel.basic_consume(queue='youtube', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    #Bucle infinita
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)