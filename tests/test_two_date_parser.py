import datetime
import pytest

from functions.two_date_parser import compose_datetime_from


def datetime_midday_from_today(add_days=0):
    today = datetime.date.today()
    return datetime.datetime(today.year, today.month, today.day + add_days, 12, 0)


date_str_tomorrow = "tomorrow"
date_str_today = "today"
valid_str_time_midday = "12:00"
datetime_today_midday = datetime_midday_from_today()
datetime_tomorrow_midday = datetime_midday_from_today(1)


@pytest.mark.parametrize(
    "date_str, time_str, expected",
    [
        (date_str_today, valid_str_time_midday, datetime_today_midday),
        (date_str_tomorrow, valid_str_time_midday, datetime_tomorrow_midday),
    ],
)
def test_compose_datetime_from(date_str: str, time_str: str, expected: datetime.datetime):
    assert compose_datetime_from(date_str, time_str) == expected
