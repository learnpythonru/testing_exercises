from functions.level_1.two_date_parser import compose_datetime_from
import pytest
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize(
    'date_str,time_str,expected',
    [
        (10101, "10:15", lazy_fixture('today_time')),
        ('tomorrow', "10:15", lazy_fixture('tomorrow_time')),

    ])
def test_compose_datetime_from(date_str, time_str, expected):
    assert compose_datetime_from(date_str, time_str) == expected


@pytest.mark.parametrize(
    'date_str,time_str',
    [
        ('tomorrow', "1015"),
        ('tomorrow', "hh:mm"),
    ])
def test_compose_datetime_from_valueerror(date_str, time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str, time_str)
