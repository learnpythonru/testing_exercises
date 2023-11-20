import datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.fixture
def base_date():
    return 'today', '04:20'


@pytest.fixture
def future_date():
    return 'tomorrow', '12:00'


@pytest.fixture
def wrong_data():
    return '123456', 'asdfghjkl'


def test_compose_datetime_from(base_date):
    date = datetime.date.today()
    assert compose_datetime_from(base_date[0],
                                 base_date[1]) == datetime.datetime(date.year,
                                                                    date.month,
                                                                    date.day,
                                                                    int('04'),
                                                                    int('20'))


def test_compose_datetime_tomorrow(future_date):
    date = datetime.date.today()
    full_date = datetime.datetime(date.year,
                                  date.month,
                                  date.day,
                                  int('12'),
                                  int('00'))
    assert compose_datetime_from(future_date[0],
                                 future_date[1]) - full_date == \
           datetime.timedelta(days=1)


def test_compose_datetime_wrong_data(wrong_data):
    with pytest.raises(ValueError):
        compose_datetime_from(wrong_data[0], wrong_data[1])
