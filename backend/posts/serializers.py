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
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "author",
            "created_at_formatted",
            "likes",
            "likes_count",
        )

    def get_likes_count(self, obj):
        return obj.likes.count()


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post_comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField() 

    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "author",
            "created_at_formatted",
            "post_comments",
            "likes_count",
            "comments_count",
        )

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.post_comments.count()