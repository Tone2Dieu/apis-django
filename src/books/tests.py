from django.test import TestCase
from django.urls import reverse
from .models import Book
# Create your tests here.


class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent Subtitle",
            author="Tom Christie",
            isbn="1234567890123"
        )


    def test_book_content(self):
        self.assertEquals(self.book.title, "A good title")
        self.assertEquals(self.book.subtitle, "An excellent Subtitle")
        self.assertEquals(self.book.author, "Tom Christie")
        self.assertEquals(self.book.isbn, "1234567890123")


    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'excellent Subtitle')
        self.assertTemplateUsed(response, "books/book_list.html")

