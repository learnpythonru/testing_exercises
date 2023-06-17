from functions.level_1_5.five_replace_word import replace_word
import pytest


@pytest.mark.parametrize(
    'text, replace_from, replace_to, expected_result',
    [
        (
            'Установите последнюю версию PowerShell для новых функций и улучшения!',
            'Установите',
            'Удалите',
            'Удалите последнюю версию PowerShell для новых функций и улучшения!',
        ),
        ('', 'PowerShell', 'WinRar', ''),
        ('Установите', 'PowerShell', 'WinRar', 'Установите'),
    ],
)
def test__replace_word__success(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(
    'text, replace_from, replace_to, exception_type',
    [
        (1111, 'PowerShell', 'WinRar', AttributeError),
        ('Установите последнюю версию PowerShell', 'Установите', 1111, TypeError),
    ],
)
def test__replace_word__exceptions(text, replace_from, replace_to, exception_type):
    with pytest.raises(exception_type):
        replace_word(text, replace_from, replace_to)
