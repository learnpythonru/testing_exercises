from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest


@pytest.mark.parametrize(
  "date_str, time_str,  expected_result",
   [
       ('date_str_tomorrow', 'time_str_19_55', 'expected_result_19_55_tomorrow'),
       ('date_str_random', 'time_str_19_55', 'expected_result_19_55_today')
  ]      
)
def test__compose_datetime_from__is_valid(date_str, time_str, expected_result, request):
    date_str = request.getfixturevalue(date_str)
    time_str = request.getfixturevalue(time_str)
    expected_result = request.getfixturevalue(expected_result)
    assert compose_datetime_from(date_str, time_str) == expected_result



@pytest.mark.parametrize(
  "date_str, time_str, expected_error, need_time_str",
  [
    ('date_str_random', 'time_int_random', AttributeError, True),
    ('time_str_19_55', 'time_int_random', TypeError, False)

  ]
)
def test__compose_datetime_from__error(date_str, time_str, expected_error, need_time_str, request):
    date_str = request.getfixturevalue(date_str)
    time_str = request.getfixturevalue(time_str)
    with pytest.raises(expected_error):
        if need_time_str:
            compose_datetime_from(date_str, time_str)
        else:
            compose_datetime_from(date_str)
