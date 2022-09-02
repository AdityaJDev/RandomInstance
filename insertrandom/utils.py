from datetime import datetime, date, timedelta
from django.db.models.fields import *
from django.db.models.fields.related import *
import random
import string
import uuid


def r_char(n):
    return "".join(random.choices(string.ascii_letters, k=random.randrange(n)))


def r_int(n=10000):
    return random.randrange(n)


def r_float(n=10000.0, m=0.0):
    return random.uniform(m, n)


def r_email():
    return (
        "".join(random.choices(string.ascii_letters, k=random.randrange(10)))
        + "@"
        + "".join(random.choices(string.ascii_letters, k=random.randrange(10)))
        + ".com"
    )


def r_datetime(start=datetime.strptime("1970-1-1", "%Y-%m-%d"), end=datetime.now()):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def r_date(start=date(1970, 1, 1), end=date.today()):
    delta = start - end
    int_delta = delta.days
    random_day = random.randrange(int_delta)
    return start + timedelta(days=random_day)


def r_url():
    return (
        "https://www."
        + "".join(random.choices(string.ascii_letters, k=random.randrange(10)))
        + ".com/"
        + "".join(random.choices(string.ascii_letters, k=random.randrange(6)))
    )


def r_binary():
    return bin(r_int())


def r_bool():
    return random.choices([True, False])


def r_uuid():
    return str(uuid.uuid4())


def random_data(ClassName, n=1):
    masterlist = []
    for i in range(n):
        randict = {}
        for f in ClassName._meta.fields:
            if type(f) == (CharField or TextField):
                randict[f.name] = r_char(f.max_length)
            elif type(f) == (IntegerField or BigIntegerField or PositiveIntegerField):
                randict[f.name] = r_int()
            elif type(f) == FloatField:
                randict[f.name] = r_float()
            elif type(f) == EmailField:
                randict[f.name] = r_email()
            elif type(f) == DateTimeField:
                randict[f.name] = r_datetime()
            elif type(f) == URLField:
                randict[f.name] = r_url()
            elif type(f) == ForeignKey:
                randict[f.name] = None
            elif type(f) == (BigAutoField or AutoField):
                continue
            elif type(f) == BinaryField:
                randict[f.name] = r_binary()
            elif type(f) == (BooleanField or NullBooleanField):
                randict[f.name] = r_bool()
            elif type(f) == UUIDField:
                randict[f.name] = r_uuid()
        masterlist.append(random_data())
    return masterlist
