import datetime
from functions.two_date_parser import compose_datetime_from


def test_compose_datetime_from_today():
    date = datetime.date.today()
    assert compose_datetime_from('today', '16 : 48') == datetime.datetime(date.year, date.month, date.day, 16, 48,)


def test_compose_datetime_from():
    date = datetime.date.today() + datetime.timedelta(days=1)
    assert compose_datetime_from('tomorrow', '16 : 48') == datetime.datetime(date.year, date.month, date.day, 16, 48,)
