from twilio.rest import Client
def sru(num):


    account_sid = '################################'
    auth_token = '###############################'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Bro wake up you are feeling drowsiness',
        from_='#1234567898',
        to = str(num)
    )

    print(message.sid)
#sru(input("Enter number"))    
