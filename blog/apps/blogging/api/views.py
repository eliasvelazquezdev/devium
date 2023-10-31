from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from ..models import Post, Tag, Comment
from .serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, TagSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostListView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostCreateView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsAuthorOrReadOnly,
    ]

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer