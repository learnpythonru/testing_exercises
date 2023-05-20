from functions.level_1.five_title import change_copy_item


def test__change_copy_item__max_length_20():
    title = 'Hello World!'
    assert change_copy_item(title, 20) == title


def test__change_copy_item__max_length_100():
    title = 'Hello World!'
    assert change_copy_item(title, 100) == 'Copy of Hello World!'


def test__change_copy_item__title_with_copy_and_index():
    assert change_copy_item('Copy of Hello World! (3)', 100) == 'Copy of Hello World! (4)'
