from rest_framework import serializers
from ..models import Post, Tag, Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published', 'updated', 'author', 'tags']
class PostHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer that will return Post instances with hyperlinks to every instance in the response
    """
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'author', 'published', 'updated']

class PostDetailSerializer(serializers.ModelSerializer):
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

class TagListSerializer(serializers.ModelSerializer):
    """
    Serializer that returns a listing of tags and hyperlinks to every post related to a single tag
    """
    posts = PostHyperLinkedSerializer(many=True, read_only=True, source='tags')
    class Meta:
        model = Tag
        fields = ('name', 'posts')
