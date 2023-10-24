from django.shortcuts import render
from rest_framework import generics
from ..models import Post, Tag, Comment
from .serializers import PostSerializer, TagSerializer, CommentSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer