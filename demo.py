from twilio.rest import Client
def sru(num):


    account_sid = 'AC93775dc42b40670cf6835820cb79c098'
    auth_token = '76a6270b389c2e137a60399a1fadb8f2'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Bro wake up you are feeling drowsiness',
        from_='#1234567898',
        to = str(num)
    )

    print(message.sid)
#sru(input("Enter number"))    