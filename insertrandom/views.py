from insertrandom.models import Author, Publisher, Books
from rest_framework import generics
from insertrandom.serializer import (
    AuthorSerializer,
    BooksSerializer,
    PublisherSerializer,
)


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherrView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = BooksSerializer


class BooksView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = PublisherSerializer
