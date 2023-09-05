from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest


def today_time(time_str):
    date = datetime.date.today()
    hour_str, minute_str = time_str.strip().split(":")
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        int(hour_str),
        int(minute_str),
    )


@pytest.mark.parametrize(
    'date_str,time_str,expected',
    [
        (10101, "10:15", today_time("10:15")),
        ('tomorrow', "10:15", today_time("10:15") + datetime.timedelta(days=1)),

    ])
def test_compose_datetime_from(date_str, time_str, expected):
    assert compose_datetime_from(date_str, time_str) == expected


@pytest.mark.parametrize(
    'date_str,time_str',
    [
        ('tomorrow', "1015"),
        ('tomorrow', "hh:mm")
    ])
def test_compose_datetime_from_valueerror(date_str, time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str, time_str)
