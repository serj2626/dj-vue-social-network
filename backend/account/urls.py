from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api import me, signup, send_friendship_request

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', signup, name='signup'),
    path('me/', me, name='me'),
    path('friends/send-request/<uuid:id>', send_friendship_request, name='friends_send_request'),
]
