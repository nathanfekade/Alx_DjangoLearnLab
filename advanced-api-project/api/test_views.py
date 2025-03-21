from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create('Animal farm', 1978)
    