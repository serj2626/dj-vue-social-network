from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "author",
            "created_at_formatted",
            "likes_count",
        )
