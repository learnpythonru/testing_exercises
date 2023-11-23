from functions.level_1_5.five_replace_word import replace_word
import pytest


def test__replace_word__one_word_replaced():
    assert replace_word('one two three four', 'two', 'replace_to') == 'one replace_to three four'


def test__replace_word__two_words_replaced():
    assert replace_word('one two three Two four', 'two', 'replace_to') == 'one replace_to three replace_to four'


def test__replace_word__replace_with_upper_letters():
    assert replace_word('one two three four', 'TWo', 'replace_to') == 'one replace_to three four'


def test__replace_word__not_replaced():    
    assert replace_word('one two three four', '1234', 'replace_to') == 'one two three four'


def test__replace_word__replace_from_is_empty():       
    assert replace_word('one two three four', '', 'replace_to') == 'one two three four'


def test__replace_word__replace_to_is_empty():  
    assert replace_word('one two three four', 'two', '') == 'one  three four'


def test__replace_word__replace_to_is_int_typeerror():
        with pytest.raises(TypeError):
            replace_word('one two three four', 'two', 123)


def test__replace_word__replace_from_is_int_attributeerror():
    with pytest.raises(AttributeError):
        replace_word('one two three four', 2, '123')


def test__replace_word__text_is_int_attributeerror():
    with pytest.raises(AttributeError):
        replace_word(123314, 'two', '123')


def test__replace_word__not_enough_params_typeerror():
    with pytest.raises(TypeError):   
        replace_word('123', 'bsrbg')