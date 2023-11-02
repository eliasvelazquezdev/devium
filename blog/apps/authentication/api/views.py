from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from blog.apps.users.api.serializers import UserCreateUpdateSerializer

# Create your views here
class LoginView(APIView):
    def post(self, request):
        # Get user credentials and authenticate
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)

        # If right credentials, add session info to the request
        if user:
            login(request, user)
            return Response({"login" : "success"}, status=status.HTTP_200_OK)

        # Otherwise, throw error on request
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class LogoutView(APIView):
    def post(self, request):
        # Delete session info from request
        logout(request)

        return Response({"logout" : "success"}, status=status.HTTP_200_OK)

class SignUpView(CreateAPIView):
    serializer_class = UserCreateUpdateSerializer