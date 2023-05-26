from functions.level_1.five_title import change_copy_item


def test__change_copy_item__normal_case_success():
    assert change_copy_item('Hello World!', 20) == 'Hello World!'


def test__change_copy_item__long_title():
    assert change_copy_item('Hello World!', 100) == 'Copy of Hello World!'


def test__change_copy_item__title_with_copy_and_index():
    assert change_copy_item('Copy of Hello World! (3)', 100) == 'Copy of Hello World! (4)'
