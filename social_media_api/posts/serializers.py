from rest_framework import serializers
from .models import Post,Comment,Like
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source= 'author.username')

    class Meta: 
        model = Comment
        fields = ['post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source= 'author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['author', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['user', 'post']
        read_only_fields =['user']
    