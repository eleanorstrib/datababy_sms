from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def hello():
	resp = twilio.twiml.Response()
	incoming_message = (request.values.get('Body', None)).lower()
	incoming_message_received = request.values.get('DateSent', None)
	events = ['bottle', 'breast start', 'breast end', 'wet diaper', 'soiled diaper', 'sleep start', 'sleep end']
 	help_message = "Text one of the following phrases to record your baby's activity:", events
	
	if incoming_message in events:
		resp.message("We've recorded a  %s for your baby." % (incoming_message)
	elif incoming_message == "info":
		resp.message(help_message)
	else:
		resp.message("We didn't understand your message - text 'help' for a list of possible events or try again.")
	return str(resp)


if __name__ == "__main__":
	app.run(debug=True)