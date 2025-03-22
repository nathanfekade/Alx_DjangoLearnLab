from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.base, name='base'),
    path('post/', views.PostListView.as_view(), name= 'post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name= 'post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name= 'post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name= 'post_delete'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]