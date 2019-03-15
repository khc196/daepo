from django.conf import settings
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class Consumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'ws',
            self.channel_name
        )
        self.accept()
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'ws',
            self.channel_name
        )
        self.close()
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        async_to_sync(self.channel_layer.group_send)(
            'ws',
            {
                'type': 'notify',
                'message': message,
            }
        )
    def notify(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
