from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookTestCase(APITestCase):
    def setUp(self):
        self.test_item = Book.objects.create('Animal farm', 1978)

        self.user = User.objects.create_user(
            username = 'testuser',
            password = '123'
        )

        self.client.login(username = 'testuser', password = '123')
        
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.retrieve_url = reverse('book-detail', args=[self.test_item.id])
        self.update_url = reverse('book-update', args=[self.test_item.id])
        self.delete_url = reverse('book-delete', args=[self.test_item.id])

    def test_list_items(self):
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Animal farm')
        