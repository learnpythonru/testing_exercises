from functions.level_1_5.one_median import get_median_value
import pytest


def test__get_median_value__with_empty_items():
    assert get_median_value([]) == None


@pytest.mark.xfail
def test__get_median_value__with_even_len_of_items():  
    assert get_median_value([2, 1, 4, 3]) == 1


@pytest.mark.xfail(reason='Incorrect calculation')
def test__get_median_value__with_more_even_items():  
    assert get_median_value([2, 1, 4, 3, 5, 6]) == 3


@pytest.mark.xfail(reason='Incorrect calculation')
def test__get_median_value__with_odd_len_of_items():
    assert get_median_value([1, 3, 6, 8, 9]) == 6
