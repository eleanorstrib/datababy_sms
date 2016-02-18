from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def hello():
	resp = twilio.twiml.Response()
	incoming_message = request.values.get('Body', None)
	if incoming_message is not None:
		incoming_message = incoming_message.lower()
	events = ['bottle', 'breast start', 'breast end', 'wet diaper', 'soiled diaper', 'sleep start', 'sleep end', 'fussy start', 'fussy end', 'dairy start', 'dairy end']
 	
	if incoming_message in events:
		resp.message("We've recorded a %s." % (incoming_message))
	else:
		resp.message("We didn't understand your message. You can text any of the following terms to record an event for your baby: %s" % (events))
	return str(resp)


if __name__ == "__main__":
	app.run(debug=True)