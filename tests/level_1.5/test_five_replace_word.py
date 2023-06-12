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
            (1111, 'PowerShell', 'WinRar', AttributeError),
            ('Установите последнюю версию PowerShell', 'Установите', 1111, TypeError),
        ],
)
def test__replace_word(text, replace_from, replace_to, expected_result):
    if expected_result == AttributeError:
        with pytest.raises(AttributeError):
            replace_word(text, replace_from, replace_to)
    elif expected_result == TypeError:
        with pytest.raises(TypeError):
            replace_word(text, replace_from, replace_to)
    else:
        assert replace_word(text, replace_from, replace_to) == expected_result
