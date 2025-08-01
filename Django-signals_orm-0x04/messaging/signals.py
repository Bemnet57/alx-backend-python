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