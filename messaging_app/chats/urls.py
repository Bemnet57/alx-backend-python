# chats/urls.py

from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router: messages within a conversation
convo_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
convo_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(convo_router.urls)),
]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ConversationViewSet, MessageViewSet

# router = DefaultRouter()
# router.register(r'conversations', ConversationViewSet, basename='conversation')
# router.register(r'messages', MessageViewSet, basename='message')

# urlpatterns = [
#     path('', include(router.urls)),
# ]



# # chats/urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ConversationViewSet, MessageViewSet

# router = DefaultRouter()
# router.register(r'conversations', ConversationViewSet, basename='conversations')
# router.register(r'messages', MessageViewSet, basename='messages')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
