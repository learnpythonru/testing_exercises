from datetime import datetime, timedelta
from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    now = datetime.now()

    today_result = compose_datetime_from("today", "12:00")
    assert today_result.date() == now.date()
    assert today_result.hour == 12
    assert today_result.minute == 0

    tomorrow_result = compose_datetime_from("tomorrow", "13:30")
    assert tomorrow_result.date() == (now.date() + timedelta(days=1))
    assert tomorrow_result.hour == 13
    assert tomorrow_result.minute == 30