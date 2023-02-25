import datetime
from functions.two_date_parser import compose_datetime_from


def test_compose_datetime_from_today(today):
    assert compose_datetime_from('today', '16 : 48') == datetime.datetime(today.year, today.month, today.day, 16, 48)


def test_compose_datetime_from(yesterday):
    assert compose_datetime_from('tomorrow', '16 : 48') == datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 16, 48)
