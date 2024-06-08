from django.http import JsonResponse
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class PostListViews(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        self.get_serializer(
            data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=201)
