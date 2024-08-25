from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "body", "author", "created_at_formatted")


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "author",
            "created_at_formatted",
            "likes_count",
            "comments_count",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "author",
            "created_at_formatted",
            "likes_count",
            "comments",
            "comments_count",
        )
