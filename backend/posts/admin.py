from django.contrib import admin

from .models import Comment, Post, PostAttachment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin View for Comment"""

    list_display = ("id", "created_at", "author", "get_body")

    def get_body(self, obj):
        return obj.body[:26]

    get_body.short_description = "Текст комментария"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post"""

    list_display = (
        'id',
        "get_body",
        "created_at",
        "author",
        "get_count_likes",
    )

    list_editable = ("author", )

    def get_body(self, obj):
        return obj.body[:10]

    def get_count_likes(self, obj):
        return obj.likes.all().count()

    get_body.short_description = "Текст поста"
    get_count_likes.short_description = "Кол-во лайков"


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
