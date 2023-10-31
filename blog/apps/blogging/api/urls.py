from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/detail/<int:pk>', PostDetailView.as_view(), name='post-detail')
]
