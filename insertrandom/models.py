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
        objectlist = Author.objects.all()
        idlist = []
        for i in objectlist:
            idlist.append(i.id)
        if not idlist:
            return None
        else:
            return random.choice(idlist)

    def random_data(self):
        randict = {}
        for f in self._meta.fields:
            if type(f) == (CharField or TextField):
                randict[f.name] = r_char()
            elif type(f) == (IntegerField or BigIntegerField or PositiveIntegerField):
                randict[f.name] = r_int()
            elif type(f) == FloatField:
                randict[f.name] = r_float()
            elif type(f) == EmailField:
                randict[f.name] = r_email()
            elif type(f) == DateTimeField:
                randict[f.name] = r_past_date()
            elif type(f) == URLField:
                randict[f.name] = r_url()
            elif type(f) == ForeignKey:
                randict[f.name] = f.related_model.random_object()
            elif type(f) == (BigAutoField or AutoField):
                continue
            elif type(f) == BinaryField:
                randict[f.name] = r_binary()
            elif type(f) == (BooleanField or NullBooleanField):
                randict[f.name] = r_bool()
            elif type(f) == UUIDField:
                randict[f.name] = r_uuid()
        return randict


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    publisher_email = models.EmailField(max_length=255)
    publisher_site = models.URLField(max_length=255)

    @staticmethod
    def random_object():
        objectlist = Author.objects.all()
        idlist = []
        for i in objectlist:
            idlist.append(i.id)
        if not idlist:
            return None
        else:
            return random.choice(idlist)

    def random_data(self):
        randict = {}
        for f in self._meta.fields:
            if type(f) == (CharField or TextField):
                randict[f.name] = r_char()
            elif type(f) == (IntegerField or BigIntegerField or PositiveIntegerField):
                randict[f.name] = r_int()
            elif type(f) == FloatField:
                randict[f.name] = r_float()
            elif type(f) == EmailField:
                randict[f.name] = r_email()
            elif type(f) == DateTimeField:
                randict[f.name] = r_past_date()
            elif type(f) == URLField:
                randict[f.name] = r_url()
            elif type(f) == ForeignKey:
                randict[f.name] = f.related_model.random_object()
            elif type(f) == (BigAutoField or AutoField):
                continue
            elif type(f) == BinaryField:
                randict[f.name] = r_binary()
            elif type(f) == (BooleanField or NullBooleanField):
                randict[f.name] = r_bool()
            elif type(f) == UUIDField:
                randict[f.name] = r_uuid()
        return randict


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

    def random_data(self):
        randict = {}
        for f in self._meta.fields:
            if type(f) == (CharField or TextField):
                randict[f.name] = r_char()
            elif type(f) == (IntegerField or BigIntegerField or PositiveIntegerField):
                randict[f.name] = r_int()
            elif type(f) == FloatField:
                randict[f.name] = r_float()
            elif type(f) == EmailField:
                randict[f.name] = r_email()
            elif type(f) == DateTimeField:
                randict[f.name] = r_past_date()
            elif type(f) == URLField:
                randict[f.name] = r_url()
            elif type(f) == ForeignKey:
                randict[f.name] = f.related_model.random_object()
            elif type(f) == (BigAutoField or AutoField):
                continue
            elif type(f) == BinaryField:
                randict[f.name] = r_binary()
            elif type(f) == (BooleanField or NullBooleanField):
                randict[f.name] = r_bool()
            elif type(f) == UUIDField:
                randict[f.name] = r_uuid()
        return randict
