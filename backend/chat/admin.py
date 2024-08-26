from django.contrib import admin

from .models import Conversation, ConversationMessage


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Admin View for Conversation"""

    list_display = (
        "id",
        "created_at",
        "modified_at",
    )


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    """Admin View for ConversationMessage"""

    list_display = (
        "id",
        "conversation",
        "body",
        "sent_to",
        "created_at",
        "created_by",
    )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
