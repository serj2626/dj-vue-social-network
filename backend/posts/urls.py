from django.urls import path

from .api import (
    PostDetailView,
    PostListProfileView,
    PostListView,
    post_create_comment,
    toggle_like,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("detail/<uuid:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "detail/<uuid:pk>/comment/create/",
        post_create_comment,
        name="post-create-comment",
    ),
    path("detail/<uuid:pk>/like/", toggle_like, name="toggle-like-post"),
    path("profile/<uuid:pk>/", PostListProfileView.as_view(), name="post-list-profile"),
]
