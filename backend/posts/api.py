from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.serializers import UserSerializer

from .models import Comment, Like, Post
from .serializers import PostDetailSerializer, PostSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        self.get_serializer(data=self.request.data, context={"request": self.request})
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


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    @extend_schema(summary="Просмотр поста по id")
    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        post = Post.objects.get(id=self.kwargs["pk"])

        if post.likes.filter(created_by=current_user).exists():
            is_liked = True
        else:
            is_liked = False
        return Response({"post": self.get_serializer(post).data, "is_liked": is_liked})

    @extend_schema(summary="Редактирование поста по id")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(summary="Удаление поста по id")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(summary="Частичное редактирование поста по id")
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


@extend_schema(summary="Создание комментария к посту")
@api_view(["POST"])
def post_create_comment(request, pk):
    comment = Comment.objects.create(body=request.data.get("body"), author=request.user)

    post = Post.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count += 1
    post.save()

    return Response({"msg": "Комментарий успешно создан"}, status=201)


@extend_schema(summary="Добавление или удаление лайка к посту")
@api_view(["POST"])
def toggle_like(request, pk):

    post = Post.objects.get(pk=pk)

    if not post.likes.filter(created_by=request.user):
        like = Like.objects.create(created_by=request.user)
        post.likes_count += 1
        post.likes.add(like)
        post.save()
        return Response({"msg": "Вы поставили лайк"}, status=201)
    else:
        like = Like.objects.get(created_by=request.user)
        post.likes_count -= 1
        post.likes.remove(like)
        like.delete()
        post.save()
        return Response({"msg": "Вы успешно удалили свой лайк"}, status=204)


# class ToggleLikeForPostView(generics.CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     @extend_schema(summary="Добавление лайка к посту")
#     def post(self, request, *args, **kwargs):
#         post = Post.objects.get(id=self.kwargs["pk"])
#         likes = post.likes.filter(created_by=self.request.user)
#         if likes.exists():
#             like = Like.objects.get(created_by=self.request.user)
#             post.likes.remove(like)
#             post.likes_count -= 1
#             like.delete()
#             post.save()

#             return Response({"msg": "Вы успешно удалили свой лайк"}, status=204)

#         new_like = Like.objects.create(created_by=self.request.user)
#         post.likes.add(new_like)
#         post.likes_count += 1
#         post.save()

#         return Response({"msg": "Вы поставили лайк"}, status=201)
