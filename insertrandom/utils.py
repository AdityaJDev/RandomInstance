from datetime import datetime
from django.db.models.fields import *
from django.db.models.fields.related import *
import random
import string
import uuid


def r_char():
    return "".join(random.choices(string.ascii_letters, k=16))


def r_int():
    return random.randrange(10000)


def r_float():
    return random.uniform(0.0, 10000.0)


def r_email():
    return (
        "".join(random.choices(string.ascii_letters, k=5))
        + "@"
        + "".join(random.choices(string.ascii_letters, k=5))
        + ".com"
    )


def r_past_date():
    return datetime.now() - random.randrange(10000)


def r_url():
    return (
        "https://www."
        + "".join(random.choices(string.ascii_letters, k=10))
        + ".com/"
        + "".join(random.choices(string.ascii_letters, k=6))
    )


def r_binary():
    return bin(r_int())


def r_bool():
    return random.choices([True, False])


def r_uuid():
    return str(uuid.uuid4())


# The function below is supposed to be added to model classes


def random_data(ClassName):
    randict = {}
    for f in ClassName._meta.fields:
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


def testing(ClassName, n=1):
    masterlist = []
    for i in range(n):
        obj = ClassName()
        masterlist.append(obj.random_data())
    return masterlist
