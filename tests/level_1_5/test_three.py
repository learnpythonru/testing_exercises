from functions.level_1_5.three_first import first, NOT_SET
import pytest


def test__first__only_items():
    assert first([1,2,3]) == 1


def test__first__items_and_no_set():   
    assert first([1,2,3], NOT_SET) == 1


def test__first__no_items_empty_list():       
    assert first([], 'default') == 'default'


def test__first__items_empty(): 
    assert first('', 'default') == 'default'

def test__first__items_is_none(): 
    assert first(None, 'default') == 'default'


def test__first__default_is_int():
    assert first(None, 1234) == 1234

def test__first__items_and_defaults_are_none():
    assert first(None, None) == None

def test__first__defaults_is_tuple():
    assert first(None, (5,56)) == (5, 56)


def test__first__defaults_is_string():
    assert first('default') == 'd'

 
def test__first__defaults_is_not_set():   
    assert first(NOT_SET) == 'N'


def test__first__items_is_empty_no_defaults_attributeerror():  
    with pytest.raises(AttributeError):
        first([])


def test__first__items_is_empty_attributeerror():  
    with pytest.raises(AttributeError):  
        first([], NOT_SET)


def test__first__no_parameters():  
    with pytest.raises(TypeError):
        first()