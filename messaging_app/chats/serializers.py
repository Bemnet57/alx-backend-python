# chats/serializers.py

from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Invalid email format")
        return value

    class Meta:
        model = User
        fields = [
            'user_id', 'first_name', 'last_name', 'email',
            'phone_number', 'role', 'created_at'
        ]

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'user_id',
#             'first_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'role',
#             'created_at',
#         ]

class MessageSerializer(serializers.ModelSerializer):
    sender_email = serializers.CharField(source='sender.email', read_only=True)
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender_email', 'message_body', 'sent_at']

# class MessageSerializer(serializers.ModelSerializer):
#     sender = UserSerializer(read_only=True)

#     class Meta:
#         model = Message
#         fields = [
#             'message_id',
#             'sender',
#             'message_body',
#             'sent_at',
#         ]

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']

    def get_messages(self, obj):
        messages = obj.message_set.all().order_by('sent_at')
        return MessageSerializer(messages, many=True).data


# class ConversationSerializer(serializers.ModelSerializer):
#     participants = UserSerializer(many=True, read_only=True)
#     messages = MessageSerializer(source='message_set', many=True, read_only=True)

#     class Meta:
#         model = Conversation
#         fields = [
#             'conversation_id',
#             'participants',
#             'created_at',
#             'messages',
#         ]
