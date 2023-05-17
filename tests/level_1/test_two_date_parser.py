from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest

def test_two_date_with_coma():
    assert compose_datetime_from("2023,12,15", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,55)


def test_two_date_is_tomorrow():
    assert compose_datetime_from("tomorrow", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day+1,19,55)


def test_two_date_is_chaos():
    assert compose_datetime_from("202yhbmj5", "19:33") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,33)

# ВОПРОС 4:
# Вот я поковыряла функцию, пока не разобралась, но не хочу терять наброски.
# Какой способ сохранения недоделок будет приемлем?
# Вот так комментить вообще не вариант же.


#def test_two_valueerror():
#    with pytest.raises(ValueError,AttributeError,  match="AttributeError()") as value_err_info:
#        print("with pytest!")
#        compose_datetime_from("202yhbmj5", 14645)
#     #   raise ValueError("ValueError!!!")
#        assert str(value_err_info.value) == 'some info'
#      #  assert str(value_err_info.type) == 'some info type' 
#        compose_datetime_from("202yhbmj5", 14645)
#        compose_datetime_from("202yhbmj5", "1gws43")
        