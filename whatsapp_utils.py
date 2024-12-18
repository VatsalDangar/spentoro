from dotenv import load_dotenv
import os
from fastapi import FastAPI
from twilio.rest import Client
load_dotenv()

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Wooh, 5k spend ... chill out.\nNoted Bud.',
#   to='whatsapp:+919328722848'
# )

# print(message.sid)
