from http import client
import os
from twilio.rest import Client

account_sid = os.enviorn.get('account_sid_1')
auth_token = os.enviorn.get('auth_token_1')
client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(
                                body = f"Hi! Your user two factor authentication code is {user_code}",
                                from_person = os.enviorn.get('from_person_1'),
                                to = f"{phone_number}"
                                )
    
                            
    

    print(message.sid)
                                

