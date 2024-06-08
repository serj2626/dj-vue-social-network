from django.http import JsonResponse
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

from rest_framework.permissions import AllowAny

class PostListViews(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
