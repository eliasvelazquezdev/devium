from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from blog.apps.blogging.models import Post
from blog.apps.blogging.api.serializers import PostHyperLinkedSerializer

User = get_user_model()

# The User creation method can be found in blog/apps/authentication/api/views.py
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff']
        extra_kwargs = {
            'date_joined': {'read_only': True},
        }

class UserDetailSerializer(serializers.ModelSerializer):
    posts = PostHyperLinkedSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email',  'first_name', 'last_name', 'about', 'posts', 'date_joined']
        extra_kwargs = {
            'date_joined': {'read_only': True},
        }
class UserCreateUpdateSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'about']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name' : {'required': True},
            'last_name' : {'required': True}
        }
