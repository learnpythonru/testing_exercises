from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test__compose_datetime_from__today():
    today = datetime.date.today()
    hour_str = '17'
    minute_str = '15'
    expected_today = datetime(today.year, today.month, today.day, int(hour_str), int(minute_str), )
    
    result = compose_datetime_from('today', "17:15")

    assert result == expected_today
    

def test__compose_datetime_from__tomorrow():
    today = datetime.date.today()
    hour_str = '17'
    minute_str = '15'
    tomorrow = today + datetime.timedelta(1) 
    expected_tomorrow = datetime(tomorrow.year, tomorrow.month, tomorrow.day, int(hour_str), int(minute_str), )

    result = compose_datetime_from('tomorrow', "17:15") 

    assert result == expected_tomorrow
