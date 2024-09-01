from django.contrib import admin

from .models import FriendshipRequest, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin View for User"""

    list_display = ("name","id",  "email", "avatar", "friends_count", "is_superuser")

    def friends_count(self, obj):
        return obj.friends.count()

    friends_count.short_description = "Кол-во друзей"


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    """Admin View for FriendshipRequest)"""

    list_display = (
        "created_by",
        "created_for",
        "created_at",
        "status",
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
