from django.urls import path
from .api import PostListViews

urlpatterns = [
    path("", PostListViews.as_view(), name="post-list"),
]
