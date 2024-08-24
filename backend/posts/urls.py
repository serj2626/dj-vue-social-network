from django.urls import path

from .api import PostListProfileView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    # path("create/", PostListView.as_view(), name="post-create"),
    path("profile/<uuid:id>/", PostListProfileView.as_view(), name="post-list-profile"),
]
