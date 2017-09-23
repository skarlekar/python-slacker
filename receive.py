import os
import json
from flask import Flask, request, Response


app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')


@app.route('/listening', methods=['POST'])
def inbound():
    slack_event = json.loads(request.data)
    print "--------REQUEST--------------"
    print json.dumps(slack_event)
    print "_____________________________"
    if slack_event.get('token') == SLACK_WEBHOOK_SECRET:
        event = slack_event.get('event')
        channel = event.get('channel')
        username = event.get('user')
        text = event.get('text')
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    else:
        print("Token received {} is not equal to {}".format(slack_event.get('token'), SLACK_WEBHOOK_SECRET))
    return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)
