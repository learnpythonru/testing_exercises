from functions.level_1.five_title import change_copy_item


def test__change_copy_item__normal_name():
    assert change_copy_item('Banana') == 'Copy of Banana'
def test__change_copy_item__copy_of_name():
    assert change_copy_item('Copy of Banana') == 'Copy of Banana (2)'
def test__change_copy_item__copy_of_copy_name():
    assert change_copy_item('Copy of Banana (7)') == 'Copy of Banana (8)'
def test__change_copy_item__normal_name_with_lenght():
    assert change_copy_item('Banana', 5) == 'Banana'