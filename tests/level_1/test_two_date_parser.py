from functions.level_1.two_date_parser import compose_datetime_from


import datetime, pytest


@pytest.mark.parametrize(
        'date_str, time_str, expected_result', 
        [
        ("today", "10:30", datetime.datetime.now().replace(hour=10, minute=30, second=0, microsecond=0)),
        ("tomorrow", "14:45", (datetime.datetime.now() + datetime.timedelta(days=1)).replace(hour=14, minute=45, second=0, microsecond=0)),
    ]
)
def test__compose_datetime__from(date_str, time_str, expected_result):
    result = compose_datetime_from(date_str, time_str)
    assert result == expected_result


def test__compose_datetime__wrong_time_format():    
    with pytest.raises(ValueError):
        compose_datetime_from("today", "10-30")

