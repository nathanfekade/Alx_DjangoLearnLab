from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,FeedView, LikePostView, UnlikePostView


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('like/<int:pk>/', LikePostView.as_view(), name='like_post'),
    path('unlike/<int:pk>/', UnlikePostView.as_view(), name='unlike_post'),
]