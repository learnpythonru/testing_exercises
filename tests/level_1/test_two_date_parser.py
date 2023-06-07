from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest


@pytest.fixture
def time_str():
    return "19:55"

@pytest.fixture
def expected_result(time_str): 
    hour_str, minute_str = time_str.strip().split(":")
    hour_str = int(hour_str)
    minute_str = int(minute_str)
    return datetime.datetime(datetime.date.today().year,
                                                datetime.date.today().month,
                                                datetime.date.today().day, 
                                                 hour_str, minute_str)


@pytest.mark.parametrize(
  "date_str, time_str,  expected_result",
   [
#      ("2023,12,15", time_str, expected_result),
      ("tomorrow", "19:55", datetime.datetime(datetime.date.today().year,
                                              datetime.date.today().month,
                                              datetime.date.today().day+1,
                                              19,55)),
     ("202yhbmj5", "19:33", datetime.datetime(datetime.date.today().year,
                                              datetime.date.today().month,
                                              datetime.date.today().day,
                                              19,33)),
  ]      
)
def test__compose_datetime_from__is_valid(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result


@pytest.mark.parametrize(
  "date_str, time_str,  expected_error, need_time_str",
  [
    ("202yhbmj5", 14645, AttributeError, 1),
    ("19:33", 0, TypeError, 0)

  ]
)
def test__compose_datetime_from__error(date_str, time_str, expected_error, need_time_str):
    with pytest.raises(expected_error):
        if need_time_str == 1:
            compose_datetime_from(date_str, time_str)
        else:
            compose_datetime_from(date_str)
