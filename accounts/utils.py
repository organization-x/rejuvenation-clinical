from http import client
from twilio.rest import Client

# for environment variable management
import os
from dotenv import load_dotenv
# find and load the environment variables from .env file
load_dotenv()

account_sid = os.getenv('account_sid_1')
auth_token = os.getenv('auth_token_1')
client = Client(account_sid, auth_token)
print(auth_token)
print(account_sid)

def send_sms(user_code, phone_number):
    message = client.messages.create(
                                body = f"Hi! Your user two factor authentication code is {user_code}",
                                from_person = os.getenv('from_person_1'),
                                to = f"{phone_number}"
                                )
    
                            
    

    print(message.sid)
                                

