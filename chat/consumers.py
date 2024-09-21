import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # accept connection
        self.connect()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send a message to the websocket
        self.send(text_data=json.dumps({'message': message}))
