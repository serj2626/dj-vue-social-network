from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.serializers import UserSerializer

from .models import Post, Like
from .serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        self.get_serializer(data=self.request.data, context={
                            "request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=201)

    @extend_schema(summary="Список постов")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(summary="Создание поста")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(summary="Список постов пользователя")
class PostListProfileView(APIView):

    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        posts = Post.objects.filter(author=id)
        user = User.objects.get(id=id)

        posts_serializer = PostSerializer(posts, many=True)
        user_serializer = UserSerializer(user)

        return Response({"posts": posts_serializer.data, "user": user_serializer.data})


class ToggleLikeForPostView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @extend_schema(summary="Добавление лайка к посту")
    def patch(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs["pk"])
        likes = post.likes.filter(created_by=self.request.user)
        if likes.exists():
            like = Like.objects.get(created_by=self.request.user)
            post.likes.remove(like)
            post.likes_count -= 1
            like.delete()
            post.save()

            return Response({"msg": "Вы успешно удалили свой лайк"}, status=200)
        
        new_like = Like.objects.create(created_by=self.request.user)
        post.likes.add(new_like)
        post.likes_count += 1
        post.save()

        return Response({"msg": "Вы поставили лайк"}, status=201)
