from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

events = ['bottle', 'breast start', 'breast end', 'wet diaper', 'soiled diaper', 'sleep start', 'sleep end']
help_message = "Text one of the following phrases to record your baby's activity:", events

@app.route("/", methods=['GET', 'POST'])
def hello():
	resp = twilio.twiml.Response()
	incoming_message = request.values.get('Body', None)
	incoming_message_received = request.values.get('DateSent', 'unknown')
	
	if incoming_message in events:
		resp.message("Got it!  We've recorded a", incoming_message, "for your baby at", incoming_message_received, ".")
	elif incoming_message =='help':
		resp.message(help_message)
	else:
		resp.message("We didn't understand your message - text 'help' for a list of possible events or try again.")
	return str(resp)


if __name__ == "__main__":
	app.run(debug=True)