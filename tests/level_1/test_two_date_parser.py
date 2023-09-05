import datetime

from functions.level_1.two_date_parser import compose_datetime_from


def check_datetime(date_str: str, time_str: str) -> datetime.datetime:
    # Had to write same function to get same datetime everyday
    date = datetime.date.today()
    if date_str == "tomorrow":
        date += datetime.timedelta(days=1)
    
    hour_str, minute_str = time_str.strip().split(":")
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        int(hour_str),
        int(minute_str),
    )

def test_compose_datetime_from():
    assert compose_datetime_from('tomorrow', '13:37') == check_datetime('tomorrow', '13:37')
