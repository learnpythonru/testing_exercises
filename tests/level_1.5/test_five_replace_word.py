from functions.level_1_5.five_replace_word import replace_word
import pytest


def test__replace_word__success():
    text = 'Установите последнюю версию PowerShell для новых функций и улучшения!'
    replace_from = 'Установите'
    replace_to = 'Удалите'
    expected_result = 'Удалите последнюю версию PowerShell для новых функций и улучшения!'
    
    result = replace_word(text, replace_from, replace_to)

    assert result == expected_result


def test__replace_word__empty_original_string():
    assert replace_word('', 'PowerShell', 'WinRar') == ''


def test__replace_word__no_matches():
    assert replace_word('Установите', 'PowerShell', 'WinRar') == 'Установите'


def test__replace_word__attribute_error():
    with pytest.raises(AttributeError):
        replace_word(1111, 'PowerShell', 'WinRar')


def test__replace_word__type_error():
    with pytest.raises(TypeError):
        replace_word('Установите последнюю версию PowerShell', 'Установите', 1111)

