from functions.level_1_5.three_first import first
import pytest


def test__first__return_first_element_of_not_empty_items_when_defaul_int():

    assert first([1, 2, 3], 1) == 1


def test__first__return_first_element_of_not_empty_items_when_defaul_is_None():

    assert first([1, 2, 3]) == 1


def test__first__return_default_value_for_empty_items_and_default_is_int():

    assert first([], 1) == 1


def test__first__items_is_None_and_default_not_set_return_exception():

    with pytest.raises(AttributeError):
        assert first(items=[])
