from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    title = 'Hello World!'
    
    assert change_copy_item(title, 20) == title
    assert change_copy_item(title, 100) == 'Copy of Hello World!'
    assert change_copy_item('Copy of Hello World! (3)', 100) == 'Copy of Hello World! (4)'
