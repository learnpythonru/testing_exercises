from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest

def test_compose_datetime_from():
    assert compose_datetime_from("2023,12,15", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,55)
    assert compose_datetime_from("tomorrow", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day+1,19,55)
    assert compose_datetime_from("202yhbmj5", "19:33") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,33)


def test_two_valueerror():
    with pytest.raises(ValueError, match="ValueError"):
        raise ValueError("ValueError!!!")
        compose_datetime_from("202yhbmj5", 14645)
        compose_datetime_from("202yhbmj5", "1gws43")
        
# Вопрос 3: не понимаю, почему этот корректный формат при сравнении с ValueError
# проходит тест
   #     assert compose_datetime_from("tomorrow", "19:55") is ValueError