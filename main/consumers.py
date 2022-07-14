from channels.generic.websocket import WebsocketConsumer
import json

class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print(self.scope['url_route']['kwargs'])
        self.send(text_data = json.dumps({
            'message': 'pong'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass