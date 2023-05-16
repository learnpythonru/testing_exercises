import datetime
from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    assert compose_datetime_from("today", "12:00") == datetime.datetime(2023, 5, 16, 12, 0)
    assert compose_datetime_from("tomorrow", "12:00") == datetime.datetime(2023, 5, 17, 12, 0)
    assert compose_datetime_from("yesterday", "12:00") == datetime.datetime(2023, 5, 16, 12, 0)