from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms", methods=["GET", "POST"])
def sms():
    resp = twilio.twiml.Response()
    resp.message("Hello!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)