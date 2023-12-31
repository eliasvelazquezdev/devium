from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, TagsListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/add', PostCreateView.as_view(), name='post-add'),
    path('posts/detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/detail/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('tags/', TagsListView.as_view(), name='tags-list'),
]
