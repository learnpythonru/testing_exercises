from functions.level_1.two_date_parser import compose_datetime_from
import datetime

def test_compose_datetime_from():
    assert compose_datetime_from("2023,12,15", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,55)
    assert compose_datetime_from("tomorrow", "19:55") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day+1,19,55)
    assert compose_datetime_from("202yhbmj5", "19:33") == datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day,19,33)
    pass
