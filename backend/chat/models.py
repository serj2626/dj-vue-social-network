import uuid

from django.db import models
from django.utils.timesince import timesince

from account.models import User


class Conversation(models.Model):
    """
    Модель Беседа
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(
        User, related_name='conversations', verbose_name='участники')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')
    modified_at = models.DateTimeField(
        auto_now=True, verbose_name='дата изменения')

    def modified_at_formatted(self):
        return timesince(self.created_at)
    
    def __str__(self):
        return f'Беседа с {self.id}'

    class Meta:
        verbose_name = 'Беседа'
        verbose_name_plural = 'Беседы'


class ConversationMessage(models.Model):
    """
    Модель Сообщения в беседе
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(
        Conversation, related_name='messages', on_delete=models.CASCADE, verbose_name='беседа')
    body = models.TextField(blank=True, null=True,
                            verbose_name='текст сообщения')
    sent_to = models.ForeignKey(User, related_name='received_messages',
                                on_delete=models.CASCADE, verbose_name='получатель')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='дата создания')
    created_by = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE, verbose_name='отправитель')

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return f'Сообщение от {self.created_by} к {self.sent_to}'

    class Meta:
        verbose_name = 'Сообщение в беседе'
        verbose_name_plural = 'Сообщения в беседе'
        ordering = ['-created_at']