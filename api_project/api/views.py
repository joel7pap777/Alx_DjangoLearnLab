from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()      # Retrieves all books
    serializer_class = BookSerializer  # Uses the serializer we created
