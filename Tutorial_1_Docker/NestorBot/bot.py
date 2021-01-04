from slack import WebClient
import os
from pathlib import Path
from dotenv import load_dotenv
import time
from flask import Flask
from slackeventsapi import SlackEventAdapter

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


#Detectar eventos via protocolo http
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        slack_web_client.chat_postMessage(channel=channel_id,text="Holanda")

if __name__ == "__main__":
    app.run(debug=True)