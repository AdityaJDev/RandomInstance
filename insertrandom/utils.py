from datetime import datetime, date, timedelta
from django.db.models.fields import *
from django.db.models.fields.related import *
import random
import string
import uuid


def r_char(n=255):
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


func_dict = {
    CharField: r_char,
    TextField: r_char,
    IntegerField: r_int,
    BigIntegerField: r_int,
    PositiveIntegerField: r_int,
    FloatField: r_float,
    EmailField: r_email,
    DateTimeField: r_datetime,
    DateField: r_date,
    URLField: r_url,
    BinaryField: r_binary,
    BooleanField: r_bool,
    NullBooleanField: r_bool,
    UUIDField: r_uuid,
}


def random_data(ClassName, n=1):
    masterlist = []
    for i in range(n):
        randict = {}
        for f in ClassName._meta.fields:
            if type(f) == ForeignKey:
                randict[f.name] = None
            elif type(f) == (BigAutoField or AutoField):
                continue
            else:
                randict[f.name] = func_dict[type(f)]()
        masterlist.append(randict)
    return masterlist
