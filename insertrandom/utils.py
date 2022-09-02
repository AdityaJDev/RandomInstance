from datetime import datetime, date, timedelta
from multiprocessing import AuthenticationError
from django.db.models.fields import *
from django.db.models.fields.related import *
import random
import string
import uuid


def r_char(kwargs):
    return "".join(
        random.choices(string.ascii_letters, k=random.randrange(kwargs.get("nc")))
    )


def r_int(kwargs):
    return random.randrange(kwargs.get("mi", 0), kwargs.get("ni", 10000))


def r_float(kwargs):
    return random.uniform(kwargs.get("mf", 0.0), kwargs.get("nf", 10000.0))


def r_email(kwargs):
    return (
        "".join(random.choices(string.ascii_letters, k=random.randrange(10)))
        + "@"
        + "".join(random.choices(string.ascii_letters, k=random.randrange(10)))
        + ".com"
    )


def r_datetime(kwargs):
    start_time = datetime.strptime(
        kwargs.get("start_t", "1970-1-1 1:30"), "%Y-%m-%d %H:%M"
    )
    if kwargs.get("start_t", None):
        end_time = datetime.strptime(kwargs.get("end_t"), "%Y-%m-%d %H:%M")
    else:
        end_time = datetime.now()
    delta = end_time - start_time
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start_time + timedelta(seconds=random_second)


def r_date(kwargs):
    start_date = datetime.strptime(kwargs.get("start_d", "1970-1-1"), "%Y-%m-%d")
    if kwargs.get("start_d", None):
        end_date = datetime.strptime(kwargs.get("end_d"), "%Y-%m-%d")
    else:
        end_date = datetime.today()
    delta = end_date - start_date
    int_delta = delta.days
    random_day = random.randrange(int_delta)
    return start_date + timedelta(days=random_day)


def r_url(kwargs):
    return (
        "https://www."
        + "".join(random.choices(string.ascii_letters, k=random.randrange(10)))
        + ".com/"
        + "".join(random.choices(string.ascii_letters, k=random.randrange(6)))
    )


def r_binary(kwargs):
    return bin(r_int(kwargs))


def r_bool(kwargs):
    return random.choices([True, False])


def r_uuid(kwargs):
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


def random_data(ClassName, n=1, **kwargs):
    masterlist = []
    for i in range(n):
        randict = {}
        for f in ClassName._meta.fields:
            if type(f) == ForeignKey:
                randict[f.name] = None
            elif type(f) == (BigAutoField or AutoField):
                continue
            else:
                max_l = kwargs.get("nc", f.max_length)
                kwargs["nc"] = max_l
                randict[f.name] = func_dict[type(f)](kwargs)
        masterlist.append(randict)
    return masterlist
