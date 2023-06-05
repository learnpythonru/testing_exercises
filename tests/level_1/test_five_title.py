from functions.level_1.five_title import change_copy_item
import pytest

def test__change_copy_item__add_copy(): 
    assert change_copy_item('My Item') == 'Copy of My Item'

def test__change_copy_item__increase_number_of_copy(): 
    assert change_copy_item('Copy of My Item (2)') == 'Copy of My Item (3)'

def test__change_copy_item__behavior_for_long_title(): 
    assert change_copy_item('Very long title with many words', max_main_item_title_length=10) == 'Very long title with many words'

def test__change_copy_item__for_basic_case_with_text(): 
    assert change_copy_item("Copy of My Item") == "Copy of My Item (2)"

@pytest.mark.parametrize(
    'title, max_main_item_title_length, expected_result',
    [
        ('My Item', 100, 'Copy of My Item'),
        ('Copy of My Item (2)', 100, 'Copy of My Item (3)'),
        ('Very long title with many words', 10, 'Very long title with many words'),
        ('Copy of My Item', 100, 'Copy of My Item (2)'),
    ]
)
def test__change_copy_item(title, max_main_item_title_length, expected_result):
    assert change_copy_item(title, max_main_item_title_length) == expected_result
