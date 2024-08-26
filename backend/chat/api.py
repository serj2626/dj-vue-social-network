from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.decorators import (
    api_view,
)
from rest_framework.response import Response

from account.models import User

from .models import Conversation, ConversationMessage
from .serializers import (
    ConversationDetailSerializer,
    ConversationMessageSerializer,
    ConversationSerializer,
)


class ConversationListView(generics.ListAPIView):
    """
    Представление списка бесед пользователя
    """

    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(users__in=list([self.request.user]))

    @extend_schema(summary="Список бесед пользователя")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ConversatonDetailView(generics.RetrieveAPIView):
    """
    Представление беседы пользователя
    """

    serializer_class = ConversationDetailSerializer
    queryset = Conversation.objects.all()

    def get_queryset(self):
        return Conversation.objects.filter(id=self.kwargs["pk"])

    @extend_schema(summary="Беседа пользователя")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@extend_schema(summary="Создание или получение беседы")
@api_view(["GET"])
def conversation_get_or_create(request, user_pk):
    user = User.objects.get(pk=user_pk)

    conversations = Conversation.objects.filter(users__in=list([request.user])).filter(
        users__in=list([user])
    )

    if conversations.exists():
        conversation = conversations.first()
    else:
        conversation = Conversation.objects.create()
        conversation.users.add(user, request.user)
        conversation.save()

    serializer = ConversationDetailSerializer(conversation)

    return Response(serializer.data)


@extend_schema(summary="Отправка сообщения пользователю")
@api_view(["POST"])
def conversation_send_message(request, pk):
    conversation = Conversation.objects.filter(users__in=list([request.user])).get(
        pk=pk
    )

    for user in conversation.users.all():
        if user != request.user:
            sent_to = user

    conversation_message = ConversationMessage.objects.create(
        conversation=conversation,
        body=request.data.get("body"),
        created_by=request.user,
        sent_to=sent_to,
    )

    serializer = ConversationMessageSerializer(conversation_message)

    return Response(serializer.data)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление сообщения
    """

    serializer_class = ConversationMessageSerializer
    queryset = ConversationMessage.objects.all()

    def get_object(self):
        return ConversationMessage.objects.filter(
            conversation__users__in=list([self.request.user])
        )

    @extend_schema(summary="Получения сообщения по id")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(summary="Редактирование сообщения по id")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(summary="Частичное редактирование сообщения по id")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(summary="Удаление сообщения по id")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
