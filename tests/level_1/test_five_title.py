from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('My Item') == 'Copy of My Item'
    assert change_copy_item('Copy of My Item (2)') == 'Copy of My Item (3)'

    assert change_copy_item('Very long title with many words', max_main_item_title_length=10) == 'Very long title with many words'

    assert change_copy_item("Copy of My Item") == "Copy of My Item"
    