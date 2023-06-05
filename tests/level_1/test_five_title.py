from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected_result",
    [
        ('THIS IS TITLE', 100, 'Copy of THIS IS TITLE'),
        ('THIS IS TITLE', 10, 'THIS IS TITLE'),
        ('Copy of something(17)', 100, 'Copy of (18)'),
        ('Copy of something (17)', 100, 'Copy of something (18)'),
        ('Copy of something(1fvd7)', 100, 'Copy of something(1fvd7) (2)'),
    ]
)      
def test__change_copy_item__is_valid(title, max_main_item_title_length, expected_result):
    assert change_copy_item(title, max_main_item_title_length) == expected_result
