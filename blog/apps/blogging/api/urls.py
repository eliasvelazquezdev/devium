from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/detail/<int:pk>', PostDetail.as_view(), name='post-detail')
]
