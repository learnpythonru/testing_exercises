from functions.level_1_5.one_median import get_median_value
import pytest


"""Хотелось бы сразу заметить, что функция и нормальные тесты невозможны"""
def test__get_median_value__empty_list():
    assert get_median_value([]) is None

def test__get_median_value__list_with_odd_numbers_elem():
    assert get_median_value([3, 7, 4]) == 4

def test__get_median_value__list_with_even_numbers_elem():
    with pytest.raises(IndexError):
        get_median_value([1, 3, 5, 7])

def test__get_median_value__list_with_1_elem():
    with pytest.raises(IndexError):
        get_median_value([1])

def test__get_median_value__list_with_negative_numb():
    assert get_median_value([-5, -10, -1, -6, -8]) == -6