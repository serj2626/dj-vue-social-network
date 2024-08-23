from django.contrib import admin

from .models import User, FriendshipRequest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''

    list_display = ('id', 'email', 'name', 'avatar', 'is_superuser' )


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    '''Admin View for FriendshipRequest)'''

    list_display = ( 'created_for', 'created_at', 'created_by', 'status', )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)