from functions.level_1_5.three_first import first
import pytest


def test__first__with_items():
    assert first([5, 7, 1, 15]) == 5


def test__first__with_empty_items_and_default_is_not_set():
    with pytest.raises(AttributeError):
        first([])


def test__first__with_empty_items_and_default_is_none():
    assert first([], None) == None


def test__first__with_empty_items_and_default_is_int():
    assert first([], 0) == 0

