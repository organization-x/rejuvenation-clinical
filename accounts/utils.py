from http import client
from twilio.rest import Client

# for environment variable management
import os
from dotenv import load_dotenv
# find and load the environment variables from .env file
load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(user_code, phone_number):
    message = client.messages.create(
                                body = f"Hi! Your user two factor authentication code is {user_code}",
                                from_person = os.getenv('FROM_PERSON'),
                                to = f"{phone_number}"
                                )

    print(message.sid)
