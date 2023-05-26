from functions.level_1_5.three_first import first
import pytest


def test__first__with_items():
    items = [5, 7, 1, 15]
    assert first(items) == 5


def test__first__with_empty_items_and_default_is_NOT_SET():
    items = []
    default = "NOT_SET"
    with pytest.raises(AttributeError):
        first(items)


def test__first__with_empty_items_and_default_is_None():
    items = []
    default = None
    assert first(items, default) == None


def test__first__with_empty_items_and_default_is_int():
    items = []
    default = 0
    assert first(items, default) == 0

