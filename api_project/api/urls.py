from django.urls import path
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books' )

urlpatterns = router.urls

# urlpatterns = [
#     # path('books/', BookList.as_view(), name='book-list'),  
# ]