from .models import FriendshipRequest


def get_current_friendsgip_requests(user):
    return user.friends.filter(status=FriendshipRequest.ACCEPTED)