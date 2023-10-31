from rest_framework import serializers
from ..models import Post, Tag, Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published', 'updated', 'author', 'tags']

class PostCreateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        for tag_data in tags_data:
            post.tags.add(Tag.objects.create(**tag_data))
        post.save()
        return post
class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published', 'updated', 'author', 'tags', 'comments']
