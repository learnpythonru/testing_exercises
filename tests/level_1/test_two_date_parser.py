import datetime
from freezegun import freeze_time


@freeze_time("2012-01-01")
def test_compose_datetime_from():
    from functions.level_1.two_date_parser import compose_datetime_from

    assert compose_datetime_from("", time_str="18:12") == datetime.datetime(2012, 1, 1, 18, 12)
    assert compose_datetime_from("tomorrow", time_str="18:12") == datetime.datetime(2012, 1, 2, 18, 12)
