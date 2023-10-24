from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.apps.blogging.models import Post

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = '__all__'