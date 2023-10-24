from django.urls import path
from .views import PostList

urlpatterns = [
    path('posts', PostList.as_view(), name='post-list'),
    path('posts/add', PostList.as_view(), name='post-create'),
]
