import datetime
from freezegun import freeze_time
from functions.level_1.two_date_parser import compose_datetime_from
import pytest

@pytest.mark.parametrize(
        "date_str,time_str,expected_result",
        [
            ("today", "12:00", datetime.datetime(2023, 5, 16, 12, 0)),
            ("tomorrow", "12:00", datetime.datetime(2023, 5, 17, 12, 0)),
            ("yesterday", "12:00", datetime.datetime(2023, 5, 16, 12, 0)),
        ],
        ids=[
            'datetime_from_today',
            'datetime_from__tomorrow',
            'datetime_from_yesterday',
        ]
)
@freeze_time("2023-05-16")
def test_compose_datetime_from__successfull(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result

