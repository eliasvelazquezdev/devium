from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from ..models import Post, Tag
from .serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, PostUpdateSerializer, TagListSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostListView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsAuthorOrReadOnly,
    ]

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostCreateView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrReadOnly, 
    ]

    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer


class TagsListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer