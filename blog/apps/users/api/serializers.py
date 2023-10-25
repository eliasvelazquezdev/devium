from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from blog.apps.blogging.models import Post

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'about', 'posts', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'first_name' : {'required': True},
            'last_name' : {'required': True}
        }