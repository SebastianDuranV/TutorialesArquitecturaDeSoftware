from slack import WebClient
import os
from pathlib import Path
from dotenv import load_dotenv
import time
from flask import Flask
from slackeventsapi import SlackEventAdapter
import pika

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKENB"))
BOT_ID = slack_web_client.api_call("auth.test")['user_id']

slack_event_adapter = SlackEventAdapter(
    os.environ.get("SIGNING_SECRET"),'/slack/events',app) 

#Enviar mensaje
#slack_web_client.chat_postMessage(channel='#test',text="Holanda")

#Crear conexión 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='read')

#Detectar eventos via protocolo http
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        message = channel_id + ',' + user_id + ',' + text
        channel.basic_publish(exchange='',routing_key='read',body=message)

if __name__ == "__main__":
    app.run(debug=True)