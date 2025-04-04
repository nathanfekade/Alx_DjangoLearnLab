from django.urls import path
from .views import RegisterView, LoginView, RetrieveTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', RetrieveTokenView.as_view(), name='retrieve_token'),
]