from datetime import datetime, timedelta

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize('date_str, time_str, expected_result', [
    ('tomorrow', '00:00', (datetime(datetime.now().year, datetime.now().month,
                           datetime.now().day) + timedelta(days=1)).replace(
                               hour=00, minute=00, second=00,)),
    ('today', '12:25', (datetime(datetime.now().year, datetime.now().month,
                                 datetime.now().day).replace(
                                     hour=12, minute=25, second=00))),
    ('2023-11-18', '13:45', (datetime(datetime.now().year,
                                      datetime.now().month,
                                      datetime.now().day).replace(
                                     hour=13, minute=45, second=00))),
])
def test_compose_datetime_from(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str=date_str,
                                 time_str=time_str) == expected_result


@pytest.mark.parametrize('date_str, time_str', [
    ('2023-11-18', '13:45:00'),
    ('yesterday', ''),
])
def test_compose_datetime_from_with_error(date_str, time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str=date_str, time_str=time_str)
