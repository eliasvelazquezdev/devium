from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import UserSerializer
from .permissions import IsAccountOwner, IsAccountOwnerOrAdminUser

# Create your views here.
User = get_user_model()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated, 
        IsAccountOwner,
    ]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        IsAccountOwnerOrAdminUser,
    ]

    queryset = User.objects.all()
    serializer_class = UserSerializer