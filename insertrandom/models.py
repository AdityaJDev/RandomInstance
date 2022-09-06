from django.db import models
from django.db.models.fields import *
from django.db.models.fields.related import *
from insertrandom.utils import *
import random


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_email = models.EmailField(max_length=255)

    class Meta:
        app_label = "insertrandom"

    @staticmethod
    def random_object(n=0):
        result = None
        if n > 0:
            objlist = Author.objects.all().order_by("-id")[:n]
        else:
            objlist = Author.objects.all()
        idlist = []
        for i in objlist:
            idlist.append(i.id)
        if len(idlist) > 0:
            result = random.choices(idlist)[0]
        return result


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    publisher_email = models.EmailField(max_length=255)
    publisher_site = models.URLField(max_length=255)

    @staticmethod
    def random_object(n=0):
        result = None
        if n:
            objlist = Author.objects.all().order_by("-id")[:n]
        else:
            objlist = Author.objects.all()
        idlist = []
        for i in objlist:
            idlist.append(i.id)
        if idlist:
            result = random.choices(idlist)[0]
        return result


class Books(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    book_price = models.IntegerField()
    book_isbn = models.UUIDField()
    book_published_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=1)

    class Meta:
        unique_together = (
            "book_name",
            "author",
            "book_isbn",
        )
