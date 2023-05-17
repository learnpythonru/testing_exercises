from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    assert compose_datetime_from('today', "17:15")
    assert compose_datetime_from('tomorrow', "17:15")
