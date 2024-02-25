from functions.level_1_5.three_first import first
import pytest

def test__first__list_of_numbers():
    assert first([1, 2, 3, 4, 5]) == 1

def test__first__list_of_numbers_with_default_value():
    assert first([1, 2, 3, 4, 5], 10) == 1

def test__first__empty_list_with_default_value():
    assert first([], 'There is no numbers') == 'There is no numbers'

def test__first__empty_list_without_default_value():
    with pytest.raises(AttributeError):
        first([])

