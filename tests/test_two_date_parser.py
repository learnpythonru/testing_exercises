from functions.two_date_parser import compose_datetime_from
import pytest


@pytest.mark.parametrize(
    'date_str, time_str, expected_result',
    [
        ('today', '16 : 48', pytest.lazy_fixture('date_today')),
        ('tomorrow', '16 : 48', pytest.lazy_fixture('date_tomorrow')),
    ]
)
def test_compose_datetime_from(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result
