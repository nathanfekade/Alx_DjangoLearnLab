from rest_framework import viewsets
from rest_framework import permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import Post,Comment
from rest_framework import status
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return serializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save(author=self.request.user)

        Notification.objects.create(
                recipient = comment.post.author,
                actor= self.request.user,
                verb="Commented on",
                target_content_type=ContentType.objects.get_for_model(Comment),
                target_object_id= comment.id
            )
        return serializer

class FeedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LikePostView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)

            if Like.objects.create(user=request.user, post=post).exists():
                return Response({"detail": "post already liked"}, status=status.HTTP_400_BAD_REQUEST)
            
            like = Like.objects.create(user=request.user, post=post)
            Notification.objects.create(recipient=post.author, actor=request.user, verb='liked', target_content_type=ContentType.objects.get_for_model(Post), target_object_id=post.id)
            return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({"detail": "post not found"}, status=status.HTTP_404_NOT_FOUND)

class UnlikePostView(APIView):
    authentication_classes= [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            like = Like.objects.filter(user=request.user, post=post).first()

            if not like:
                return Response({"detail": "post is already not liked"}, status=status.HTTP_400_BAD_REQUEST)
            like.delete()
            return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"detail": "post not found"}, status=status.HTTP_404_NOT_FOUND)