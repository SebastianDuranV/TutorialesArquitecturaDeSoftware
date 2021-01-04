from slack import WebClient
#from nestorbot import NestorBot
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new NestorBot
#nestor_bot = NestorBot("#playground")

# Get the onboarding message payload
#message = nestor_bot.get_message_payload()

# Post the onboarding message in Slack
#slack_web_client.chat_postMessage(**message)

slack_web_client.chat_postMessage(channel='#test',text="Holanda")
