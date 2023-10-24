from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from ..models import Post, Tag, Comment
from .serializers import PostSerializer, TagSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsAuthorOrReadOnly,
    ]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsAuthorOrReadOnly,
    ]

    queryset = Post.objects.all()
    serializer_class = PostSerializer