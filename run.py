from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
	resp = twilio.twiml.Response()
	incoming_message = request.values.get('Body', None)
	if incoming_message == 'bottle':
		resp.message("Got it - bottle!")
		print incoming_message
	else:
		resp.message("I didn't understand.")
		print incoming_message
	return str(resp)


if __name__ == "__main__":
	app.run(debug=True)