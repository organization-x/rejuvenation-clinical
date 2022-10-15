from http import client
import os
from twilio.rest import Client

account_sid = "ACcb5c874c3fa790c9cd29979e0adad8a6"
auth_token = "39a7965c3aebe207eb917792cdadc35c"
client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(
                                body = f"Hi! Your user two factor authentication code is {user_code}",
                                from_person = "+17068885742",
                                to = f"{phone_number}"
                                )
    
                            
    

    print(message.sid)
                                

