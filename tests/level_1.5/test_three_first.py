from functions.level_1_5.three_first import first
import pytest


def test__first__success_normal():
    assert first([1, 2, 3, 4]) == 1

    
def test__first__attribute_error():
    with pytest.raises(AttributeError):
        first([])


def test__first__success_default_none():
    assert first([], None) is None


def test__first__success_list_of_string():
    assert first(['88', '2', '3', '4']) == '88'


def test__first__success_default_string():
    assert first([], 'def') == 'def'


def test__first__success_default_tuple():
    assert first([], (1, 5)) == (1, 5)


def test__first__attribute_error():
    with pytest.raises(KeyError):
        first({'a': 'b'})
