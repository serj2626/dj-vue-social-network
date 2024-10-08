from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api import (RegisterView, friends, me, send_friendship_request,
                  subscribers, subscriptions, accept_friendship_request,
                  delete_friendship_request, reject_friendship_request)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", me, name="me"),
    path("friends/<uuid:pk>", friends, name="friends-list"),
    path("subscribers/<uuid:pk>", subscribers, name="subscribers_list"),
    path("subscriptions/<uuid:pk>", subscriptions, name="subscriptions_list"),
    path(
        "friends/send-request/<uuid:id>",
        send_friendship_request,
        name="friends_send_request",
    ),
    path(
        "friends/<uuid:user_id>/accept-request/<uuid:request_id>",
        accept_friendship_request,
        name="friends_accept_request",
    ),
    path(
        "friends/reject-request/<uuid:id>",
        reject_friendship_request,
        name="friends_reject_request",
    ),
    path(
        "friends/delete-request/<uuid:id>",
        delete_friendship_request,
        name="friends_delete_request",
    ),
]
