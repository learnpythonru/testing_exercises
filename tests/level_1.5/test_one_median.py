from functions.level_1_5.one_median import get_median_value
import pytest

def test__get_median_value__empty_list():
    assert get_median_value([]) == None


def test__get_median_value__multiple_of_two():
    assert get_median_value([8, 1, 3, 2, 5, 7]) == 6


def test__get_median_value__not_multiple_of_two():
    assert get_median_value([8, 1, 3, 2, 5]) == 2


def test__get_median_value__index_error():
    with pytest.raises(IndexError):
        get_median_value([8, 1, 3, 2])
