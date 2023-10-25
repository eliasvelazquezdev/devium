from django.urls import path
from .views import UserList, UserDetail, UserUpdate, UserDelete

urlpatterns = [
    path('list/', UserList.as_view(), name='users-list'),
    path('detail/<int:pk>', UserDetail.as_view(), name='users-detail'),
    path('update/<int:pk>', UserUpdate.as_view(), name='user-update'),
    path('delete/<int:pk>', UserDelete.as_view(), name='user-delete'),
]