import pytest
import datetime

from functions.level_1.two_date_parser import compose_datetime_from

@pytest.fixture
def time_time_test_data():
    return {
        "today": "today",
        "tomorrow": "tomorrow",
        "today_date": datetime.date.today(),
        "tommorow_date": datetime.date.today() + datetime.timedelta(days=1),
        "time": "12:30",
        "expected_today_hour": 12,
        "expected_today_minute": 30,
    }

def test__compose_datetime_from__pass_tommorow_the_date_changes_to_tomorrow(time_test_data):
    result = compose_datetime_from(time_test_data["tomorrow"], time_test_data["time"])
    assert result.date() == time_test_data["tommorow_date"]

def test__compose_datetime_from__pass_tommorow_hours_does_not_change(time_test_data):
    result = compose_datetime_from(time_test_data["tomorrow"], time_test_data["time"])
    assert result.hour() == time_test_data["expected_today_hour"]

def test__compose_datetime_from__pass_tommorow_minites_does_not_change(time_test_data):
    result = compose_datetime_from(time_test_data["tomorrow"], time_test_data["time"])
    assert result.minute() == time_test_data["expected_today_minute"]

def test__compose_datetime_from__(time_test_data):
    result = compose_datetime_from(time_test_data["today"], time_test_data["time"])  
    assert result.date() == time_test_data["today_date"]

def test__compose_datetime_from__pass_today_hours_does_not_change(time_test_data):
    result = compose_datetime_from(time_test_data["today"], time_test_data["time"])  
    assert result.hour() == time_test_data["expected_today_hour"]

def test__compose_datetime_from__pass_today_minites_does_not_change(time_test_data):
    result = compose_datetime_from(time_test_data["today"], time_test_data["time"])    
    assert result.minute == time_test_data["expected_today_minute"]