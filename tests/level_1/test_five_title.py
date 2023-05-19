from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('Banana') == 'Copy of Banana'
    assert change_copy_item('Copy of Banana') == 'Copy of Banana (2)'
    assert change_copy_item('Copy of Banana (7)') == 'Copy of Banana (8)'
    assert change_copy_item('Banana', 5) == 'Banana'