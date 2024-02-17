from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest


@pytest.mark.parametrize(
    'date_str, time_str, expected_result',
    [
        (
            'today',
            "17:15",
            datetime.datetime(
                datetime.date.today().year,
                datetime.date.today().month,
                datetime.date.today().day,
                17,
                15,
            )
        ),
        (
            'tomorrow',
            "17:15",
            datetime.datetime(
                (datetime.date.today() + datetime.timedelta(1)).year,
                (datetime.date.today() + datetime.timedelta(1)).month,
                (datetime.date.today() + datetime.timedelta(1)).day,
                17,
                15,
            )
        ),
    ],
)
def test__compose_datetime_from(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result
