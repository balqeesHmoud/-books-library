from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

class ListOfBooksPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user and book for testing
        user = get_user_model().objects.create_user(username='testuser', password='12345')
        Book.objects.create(
            author=user,
            title='Test Book',
            description='Test Description',
            rating=5,
            publish_date='2023-01-01'
        )

    def test_list_of_books_page_status_code(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_list_of_books_page_template(self):
        response = self.client.get(reverse('books'))
        self.assertTemplateUsed(response, 'list_of_books.html')

    def test_list_of_books_page_content(self):
        response = self.client.get(reverse('books'))
        self.assertContains(response, 'Test Book')
        self.assertContains(response, 'Test Description')
