from django.contrib import admin
from .models import Post, PostAttachment


@admin.register(Post)
class PosAdmin(admin.ModelAdmin):
    '''Admin View for Post)'''

    list_display = ('attachments', 'created_at', 'author', )
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


@admin.register(PostAttachment)
class PostAttachmentAdmin(admin.ModelAdmin):
    '''Admin View for PostAttachment)'''

    list_display = ('image', 'author', )
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
