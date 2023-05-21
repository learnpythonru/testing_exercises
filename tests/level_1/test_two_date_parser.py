from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest

def test__compose_datetime_from_date_with_coma():
    assert compose_datetime_from("2023,12,15", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,55)


def test__compose_datetime_from_date_is_tomorrow():
    assert compose_datetime_from("tomorrow", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day+1,19,55)


def test__compose_datetime_from_date_is_chaos():
    assert compose_datetime_from("202yhbmj5", "19:33") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,33)


def test__compose_datetime_from_wrong_date():
    with pytest.raises(AttributeError):
        compose_datetime_from("202yhbmj5", 14645)

def test__compose_datetime_from_no_date_str():
    with pytest.raises(TypeError):
        compose_datetime_from("19:33")
