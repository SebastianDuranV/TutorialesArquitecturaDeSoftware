import pika ,os 

HOST = os.environ['RABBITMQ_HOST']

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = connection.channel()


while True:

    lugarBusqueda = input('Si desea buscar en wikipedia presione "w", si desea buscar en y presione "y"  o "x" para salir.\n')
    while lugarBusqueda not in ['w','y', 'x']:
        lugarBusqueda = input("ingrese una respuesta valida.\n")

    if lugarBusqueda == 'x':
        break

    #Creación de la cola
    if lugarBusqueda == 'w':
        channel.queue_declare(queue='wikipedia')
    else:
        channel.queue_declare(queue='youtube')

    busqueda = input("¿Qué quiere busar?: ")

    #Publicación del mensaje
    if lugarBusqueda == 'w':
        channel.basic_publish(exchange='',
                            routing_key='wikipedia',
                            body=busqueda)
    else:
        channel.basic_publish(exchange='',
                            routing_key='youtube',
                            body=busqueda)

    print("busqueda enviada")


connection.close()
