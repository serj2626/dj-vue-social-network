from django.db.models import Q
from rest_framework.response import Response

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from account.models import User
from account.serializers import UserSerializer
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.response import Response


@api_view(["POST"])
def search(request):
    query = request.data.get("query")
    all_posts = Post.objects.filter(
      Q(author__name__icontains=query)
        | Q(author__email__icontains=query)
    )

    all_users = User.objects.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    )
    users = all_users if all_users else User.objects.all()
    posts = all_posts 
    user_serializer = UserSerializer(users, many=True)
    post_serializer = PostSerializer(posts, many=True)

    return Response({"users": user_serializer.data, "posts": post_serializer.data})
