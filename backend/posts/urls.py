from django.urls import path

from .api import PostListProfileView, PostListView, ToggleLikeForPostView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("profile/<uuid:pk>/", PostListProfileView.as_view(), name="post-list-profile"),
    path("<uuid:pk>/like", ToggleLikeForPostView.as_view(), name="toggle-like-post"),
]
