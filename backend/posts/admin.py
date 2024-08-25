from django.contrib import admin

from .models import Like, Post, PostAttachment, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin View for Comment"""

    list_display = ("id", "created_at", "author", "get_body") 

    def get_body(self, obj):
        return obj.body[:26]

    get_body.short_description = "Текст комментария"

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Admin View for Like"""

    list_display = ("id", "created_by", "created_at")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post"""

    list_display = (
        "get_body",
        "id",
        "created_at",
        "author",
        "likes_count",
        
    )

    list_editable = ("author", "likes_count")

    def get_body(self, obj):
        return obj.body[:10]

    get_body.short_description = "Текст поста"


@admin.register(PostAttachment)
class PostAttachmentAdmin(admin.ModelAdmin):
    """Admin View for PostAttachment"""

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
