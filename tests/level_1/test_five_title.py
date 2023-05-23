from functions.level_1.five_title import change_copy_item


def test_change_copy_item_add_copy(): 
    assert change_copy_item('My Item') == 'Copy of My Item'

def test_change_copy_item_increase_number_of_copy(): 
    assert change_copy_item('Copy of My Item (2)') == 'Copy of My Item (3)'

def test_change_copy_item_behavior_for_long_title(): 
    assert change_copy_item('Very long title with many words', max_main_item_title_length=10) == 'Very long title with many words'

def test_change_copy_item_for_basic_case_with_text(): 
    assert change_copy_item("Copy of My Item") == "Copy of My Item (2)"
    