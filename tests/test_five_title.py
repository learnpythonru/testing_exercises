from functions.five_title import change_copy_item
import pytest


@pytest.mark.parametrize(
    'title, max_main_item_title_length, expected_result',
    [
        (pytest.lazy_fixture('long_string'), 100, pytest.lazy_fixture('long_string')),
        ('string', 100, 'Copy of string'),
        ('Copy of string (2)', 100, 'Copy of string (3)'),
        ('Copy of string', 100,'Copy of string (2)'),
        ('Copy of string (2+)', 100, 'Copy of string (2+) (2)'),
        ('(2)', 100, 'Copy of (2)'),
    ]
)
def test_change_copy_item(title, max_main_item_title_length, expected_result):
    assert change_copy_item(title, max_main_item_title_length) == expected_result
