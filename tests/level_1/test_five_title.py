from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    parameters = 'Copy of '
    test_title = 'There is something in the air tonight, my dear. I swear, I saw it with my own eyes.'
    
    assert change_copy_item(title=test_title) == parameters + test_title
