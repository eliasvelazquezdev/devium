from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.apps.blogging.models import Post

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'about', 'posts', 'date_joined']