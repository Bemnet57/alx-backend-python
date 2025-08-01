# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification
from django.db.models.signals import pre_save
from .models import Message, MessageHistory
from django.dispatch import receiver

@receiver(post_save, sender=Message)
def create_notification_on_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Message.objects.get(pk=instance.pk)
        if instance.content != old_instance.content:
            MessageHistory.objects.create(
                message=instance,
                old_content=old_instance.content
            )
            instance.edited = True


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_message(request, pk):
#     try:
#         message = Message.objects.get(pk=pk)
#     except Message.DoesNotExist:
#         return Response({'error': 'Message not found'}, status=404)

#     if request.user != message.sender:
#         return Response({'error': 'Unauthorized'}, status=403)

#     new_content = request.data.get('content')
#     if new_content and new_content != message.content:
#         message.content = new_content
#         message.edited = True
#         message.edited_by = request.user
#         message.save()

#     return Response({'message': 'Message updated successfully'})
