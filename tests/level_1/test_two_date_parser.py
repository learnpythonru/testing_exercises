from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest


@pytest.mark.parametrize(
  "date_str, time_str,  expected_result",
   [
      ("2023,12,15", "19:55", datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day, 19, 55)),
      ("tomorrow", "19:55", datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day+1,19,55)),
     ("202yhbmj5", "19:33", datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,33)),
  ]      
)

# когда делала assert is expected_result, получала по каждому туплу ошибку
#     AssertionError: assert datetime.datetime(2023, 5, 28, 19, 55) is datetime.datetime(2023, 5, 28, 19, 55)
#        +  where datetime.datetime(2023, 5, 28, 19, 55) = compose_datetime_from('tomorrow', '19:55')
# Заменила is на ==, теперь тесты проходят.
# Вопрос: это такая особенность дататайма, или почему так произошло?

def test__compose_datetime_from__is_valid(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result


def test__compose_datetime_from_wrong_date():
    with pytest.raises(AttributeError):
        compose_datetime_from("202yhbmj5", 14645)

def test__compose_datetime_from_no_date_str():
    with pytest.raises(TypeError):
        compose_datetime_from("19:33")
