from twilio.rest import TwilioRestClient
import os
 

account_sid = os.environ.get("ACCT_SID")

auth_token = os.environ.get("AUTH_TOKEN")

client = TwilioRestClient(account_sid, auth_token)

test_number = os.environ.get("TEST_NUMBER")
twilio_number = os.environ.get("TWILIO_NUMBER")
 
message = client.messages.create(body="do you have some data for me? :)",
    to=test_number,    # Replace with your phone number
    from_=twilio_number) # Replace with your Twilio number
print message.sid