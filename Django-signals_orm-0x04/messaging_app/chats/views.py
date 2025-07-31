from django.shortcuts import render

# Create your views here.
# chats/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework import viewsets, filters

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Add the current user as a participant if not provided
        conversation = serializer.save()
        if self.request.user not in conversation.participants.all():
            conversation.participants.add(self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Message.objects.filter(conversation__id=self.kwargs['conversation_pk'])
    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, conversation_id=self.kwargs['conversation_pk'])
