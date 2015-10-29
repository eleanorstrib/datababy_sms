
from twilio.rest import TwilioRestClient
import os

account_sid = os.environ.get('ACCT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

# retrieve a list of message objects from the Twilio API
client = TwilioRestClient(account_sid, auth_token)
messages = client.messages.list()

# instantiate a dictionary to hold the messages
# key is number message came from, value is a list of tuples 
# tuples consist of date_sent field and body of message
message_dict = {}

for message_object in messages:
	message_dict[message_object.from_] = message_dict.get(message_object.from_, [(message_object.date_sent, message_object.body)])

print message_dict
