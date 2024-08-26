from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api import me, send_friendship_request, friends, RegisterView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", me, name="me"),
    path("friends/", friends, name="friends-list"),
    path(
        "friends/send-request/<uuid:id>",
        send_friendship_request,
        name="friends_send_request",
    ),

]
