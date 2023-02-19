import datetime

import pytest

from functions.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    "date_str, time_str, expected",
    [
        (
            pytest.lazy_fixture("date_str_tomorrow"),
            pytest.lazy_fixture("valid_str_time_midday"),
            pytest.lazy_fixture("datetime_tomorrow_midday"),
        ),
        (
            pytest.lazy_fixture("date_str_today"),
            pytest.lazy_fixture("valid_str_time_midday"),
            pytest.lazy_fixture("datetime_today_midday"),
        ),
    ],
)
def test_compose_datetime_from(date_str: str, time_str: str, expected: datetime.datetime):
    assert compose_datetime_from(date_str, time_str) == expected
