from django.contrib import admin

from .models import Conversation, ConversationMessage


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Admin View for Conversation"""

    list_display = (
        "id",
        "get_user_one",
        "get_user_two",
        "created_at",
        "modified_at",
    )

    def get_user_one(self, obj):
        return obj.users.first()

    def get_user_two(self, obj):
        return obj.users.last()

    get_user_one.short_description = "Пользователь 1"
    get_user_two.short_description = "Пользователь 2"


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    """Admin View for ConversationMessage"""

    list_display = (
        "id",
        "conversation",
        "get_body",
        "sent_to",
        "created_by",
        "created_at",
    )

    def get_body(self, obj):
        return obj.body[:15] + "....."

    get_body.short_description = "Текст сообщения"
