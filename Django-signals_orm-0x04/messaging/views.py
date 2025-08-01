from django.shortcuts import render

# Create your views here.
# chats/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from messaging.models import Message
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from messaging.models import Message
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from messaging.models import Message





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



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_message(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response({'error': 'Message not found'}, status=404)

    # Only the sender is allowed to edit their message
    if request.user != message.sender:
        return Response({'error': 'You are not allowed to edit this message'}, status=403)

    new_content = request.data.get('content')
    if new_content is None:
        return Response({'error': 'No new content provided'}, status=400)

    # Only update if content actually changed
    if new_content != message.content:
        message.content = new_content
        message.edited = True
        message.edited_by = request.user  # 👈 Set the editor
        message.save()
        return Response({'message': 'Message updated successfully'})

    return Response({'message': 'No changes detected'}, status=200)



User = get_user_model()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"message": "Your account has been deleted."}, status=204)


# views.py or wherever we're fetching messages

# Example: Get all top-level messages with their replies
messages = (
    Message.objects
    .filter(parent_message__isnull=True)  # top-level messages only
    .select_related('sender=request.user', 'receiver')
    .prefetch_related('replies')  # fetch child replies efficiently
    .order_by('-timestamp')
)


@login_required
def unread_inbox(request):
    unread_messages = Message.unread.unread_for_user(request.user)
    return render(request, 'messaging/unread_inbox.html', {'unread_messages': unread_messages})
