from django.urls import path

from .api import (
    ConversationListView,
    ConversatonDetailView,
    MessageDetailView,
    conversation_get_or_create,
    conversation_send_message,
)

urlpatterns = [
    path("list/", ConversationListView.as_view(), name="conversation_list"),
    path("<uuid:pk>/", ConversatonDetailView.as_view(), name="conversation_detail"),
    path(
        "<uuid:pk>/send/", conversation_send_message, name="conversation_send_message"
    ),
    path(
        "<uuid:user_pk>/get-or-create/",
        conversation_get_or_create,
        name="conversation_get_or_create",
    ),
    path(
        "<uuid:pk>/message/<uuid:message_pk>/",
        MessageDetailView.as_view(),
        name="message_detail",
    ),
]
