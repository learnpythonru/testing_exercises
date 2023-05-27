from functions.level_1_5.three_first import first
import pytest


def test__first__items_not_zero_defaul_int():

    items = [1, 2, 3]
    default = 1

    assert first(items, default) == 1


def test__first__items_not_zero_defaul_is_None():

    items = [1, 2, 3]

    assert first(items) == 1


def test__first__items_default_int():

    items = []
    default = 1

    assert first(items, default) == 1


def test__first__items_is_None():

    items = []

    with pytest.raises(Exception) as error:
        first(items)

    assert error.type == AttributeError