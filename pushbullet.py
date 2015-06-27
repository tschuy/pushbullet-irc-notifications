import os
import websocket
import thread
import time
import json

token = os.environ['PBAUTH']


def on_message(ws, message):
    event = json.loads(message)

    if event['type'] == 'push' and event['push']['type'] == 'mirror':
        notification = event['push']
        print '{} | {}: {}'.format(notification['application_name'],
                                   notification['title'],
                                   notification['body'])

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print "websocket opened"

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://stream.pushbullet.com/websocket/{}".format(token),
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()

    print test
