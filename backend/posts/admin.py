from django.contrib import admin

from .models import Post, PostAttachment, Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    '''Admin View for Like'''

    list_display = ('created_by', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post)"""

    list_display = (
        "created_at",
        "author",
        "likes_count"
    )

    list_editable = ("author",)
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


@admin.register(PostAttachment)
class PostAttachmentAdmin(admin.ModelAdmin):
    """Admin View for PostAttachment)"""

    list_display = (
        "image",
        "author",
    )
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
