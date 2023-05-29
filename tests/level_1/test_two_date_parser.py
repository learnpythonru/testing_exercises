import datetime
from freezegun import freeze_time
from functions.level_1.two_date_parser import compose_datetime_from


@freeze_time("2023-05-16")
def test__compose_datetime__from_today():
    assert compose_datetime_from("today", "12:00") == datetime.datetime(2023, 5, 16, 12, 0)


@freeze_time("2023-05-16")
def test__compose_datetime_from__tomorrow():
    assert compose_datetime_from("tomorrow", "12:00") == datetime.datetime(2023, 5, 17, 12, 0)


@freeze_time("2023-05-16")
def test_compose_datetime_from_yeaterday():
    assert compose_datetime_from("yesterday", "12:00") == datetime.datetime(2023, 5, 16, 12, 0)