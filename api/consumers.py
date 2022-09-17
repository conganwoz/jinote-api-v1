import json
from nis import match
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['message_type']

        if message_type == 'receiver_connected':
          message = text_data_json['message']
          async_to_sync(self.channel_layer.group_send)(
              self.room_group_name,
              {
                  'type': 'chat_message',
                  'message': message,
                  'message_type': message_type
              }
          )
          
        elif message_type == 'sender_ice_candidate' or message_type == 'receiver_ice_candidate':
          candidate = text_data_json['candidate']
          async_to_sync(self.channel_layer.group_send)(
              self.room_group_name,
              {
                  'type': 'chat_message',
                  'candidate': candidate,
                  'message_type': message_type,
              }
          )
        elif message_type == 'sender_desc' or message_type == 'receiver_desc':
          description = text_data_json['description']
          async_to_sync(self.channel_layer.group_send)(
              self.room_group_name,
              {
                  'type': 'chat_message',
                  'description': description,
                  'message_type': message_type,
              }
          )

        else:
          message = text_data_json['message']
          async_to_sync(self.channel_layer.group_send)(
              self.room_group_name,
              {
                  'type': 'chat_message',
                  'message': message,
                  'message_type': message_type,
              }
          )

        # Send message to room group
        

    # Receive message from room group
    def chat_message(self, event):
        message = event.get('message')
        message_type = event.get('message_type')
        description = event.get('description')
        candidate = event.get('candidate')


        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'message_type': message_type,
            'description': description,
            'candidate': candidate
        }))