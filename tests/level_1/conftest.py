import pytest
import datetime


@pytest.fixture
def time_str_19_55():
    return "19:55"

@pytest.fixture
def hour_str_19_55(time_str_19_55):
   return int(time_str_19_55.strip().split(":")[0])

@pytest.fixture
def minute_str_19_55(time_str_19_55):
   return int(time_str_19_55.strip().split(":")[1])

@pytest.fixture
def date_str_tomorrow():
    return "tomorrow"

@pytest.fixture
def date_str_random():
    return "gedsf878iukf"

@pytest.fixture
def time_int_random():
    return 1234

@pytest.fixture
def expected_result_19_55_tomorrow(hour_str_19_55, minute_str_19_55): 
    return datetime.datetime(datetime.date.today().year,
                             datetime.date.today().month,
                             datetime.date.today().day+1, 
                             hour_str_19_55, 
                             minute_str_19_55)



@pytest.fixture
def expected_result_19_55_today(hour_str_19_55, minute_str_19_55): 
    return datetime.datetime(datetime.date.today().year,
                             datetime.date.today().month,
                             datetime.date.today().day, 
                             hour_str_19_55, 
                             minute_str_19_55)
