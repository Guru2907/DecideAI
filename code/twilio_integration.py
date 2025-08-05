import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
my_whatsapp_number = os.environ.get('MY_WHATSAPP_NUMBER')

if not all([account_sid, auth_token, my_whatsapp_number]):
    print("Missing environment variables. Please check your setup.")
else:
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
            content_variables='{"1":"12/1","2":"3pm"}',
            to=f'whatsapp:{my_whatsapp_number}'
        )
        print(f"Message sent! SID: {message.sid}")
    except Exception as e:
        print("Error:", e)
