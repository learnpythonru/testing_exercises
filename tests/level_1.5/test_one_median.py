from functions.level_1_5.one_median import get_median_value
import pytest


def test__get_median_value__no_items():

    items = []

    assert get_median_value(items) is None


def test__get_median_value__odd_number():

    items = [11, 9, 3, 5, 7]

    assert get_median_value(items) == 5


def test__get_median_value__even_number_less_then_6():

    items = [1, 3, 5, 7]

    with pytest.raises(Exception) as error:
        get_median_value(items)

    assert error.type == IndexError


def test__get_median_value__even_number_6_and_more():

    items = [11, 9, 3, 5, 7, 6]

    assert get_median_value(items) == 6
