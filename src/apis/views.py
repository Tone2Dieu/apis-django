from django.shortcuts import render
from books.models import Book
from .serializers import BookSerializer
from rest_framework import generics
# Create your views here.


class BookAPIList(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
