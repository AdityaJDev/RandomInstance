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
    def random_object():
        randObjList = Author.objects.all()
        idList = []
        for i in randObjList:
            idList.append(i.id)
            print(idList)
        return random.choices(idList)


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    publisher_email = models.EmailField(max_length=255)
    publisher_site = models.URLField(max_length=255)

    @staticmethod
    def random_object():
        objlist = Author.objects.all()
        idlist = []
        for i in objlist:
            idlist.append(i.id)
            print(idlist)
        return random.choices(idlist)


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
