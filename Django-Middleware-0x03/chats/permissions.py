from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to:
    - Allow only authenticated users
    - Allow access only if the user is a participant in the conversation
    """

    def has_permission(self, request, view):
        # All users must be authenticated to access the API
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # If the object is a Conversation, check user is a participant
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()

        # If the object is a Message, check user is participant in related conversation
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()

        return False






# from rest_framework import permissions

# class IsParticipant(permissions.BasePermission):
#     """
#     Custom permission to only allow users to access conversations/messages
#     they are a part of.
#     """

#     def has_object_permission(self, request, view, obj):
#         # For Conversation objects
#         if hasattr(obj, 'participants'):
#             return request.user in obj.participants.all()

#         # For Message objects: check if user is a participant in the related conversation
#         if hasattr(obj, 'conversation'):
#             return request.user in obj.conversation.participants.all()

#         return False
