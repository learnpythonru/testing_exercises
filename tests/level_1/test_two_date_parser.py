from functions.level_1.two_date_parser import compose_datetime_from


import datetime, pytest

def test_compose_datetime_from_today():
    result = compose_datetime_from("today", "10:30")
    expected = datetime.datetime.now().replace(hour=10, minute=30, second=0, microsecond=0)
    assert result == expected

def test_compose_datetime_from_tomorrow():   
    result = compose_datetime_from("tomorrow", "14:45")
    expected = (datetime.datetime.now() + datetime.timedelta(days=1)).replace(hour=14, minute=45, second=0, microsecond=0)
    assert result == expected

def test_compose_datetime_wrong_time_format():    
    with pytest.raises(ValueError):
        compose_datetime_from("today", "10-30")

