from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test__compose_datetime_from__today():
    today = datetime.date.today()
    expected_today = datetime.datetime(today.year, today.month, today.day, 17, 15)
    
    result = compose_datetime_from('today', "17:15")

    assert result == expected_today
    

def test__compose_datetime_from__tomorrow():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(1) 
    expected_tomorrow = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 17, 15)

    result = compose_datetime_from('tomorrow', "17:15") 

    assert result == expected_tomorrow
