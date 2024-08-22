from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Post
from .serializers import PostSerializer

from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@extend_schema(tags=["Posts"])
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        self.get_serializer(
            data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=201)

    @extend_schema(summary="Список постов")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(summary="Создание поста")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(tags=["Posts"], summary="Список постов пользователя")
class PostListProfileView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        uuid = self.kwargs['id']
        return Post.objects.filter(author_id=uuid)
