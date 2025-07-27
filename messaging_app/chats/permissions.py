from rest_framework import permissions

class IsParticipant(permissions.BasePermission):
    """
    Custom permission to only allow users to access conversations/messages
    they are a part of.
    """

    def has_object_permission(self, request, view, obj):
        # For Conversation objects
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()

        # For Message objects: check if user is a participant in the related conversation
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()

        return False
