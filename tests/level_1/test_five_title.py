from functions.level_1.five_title import change_copy_item


def test_title_with_additional_copy_text():
    assert change_copy_item('THIS IS TITLE', 100) == 'Copy of THIS IS TITLE'

def test_return_title():
    assert change_copy_item('THIS IS TITLE', 10) == 'THIS IS TITLE'

def test_if_has_copy_number_no_space():
    assert change_copy_item('Copy of something(17)', 100) == 'Copy of (18)'

def test_if_has_copy_number_with_space():
    assert change_copy_item('Copy of something (17)', 100) == 'Copy of something (18)'    

def test_if_no_has_copy_number():
    assert change_copy_item('Copy of something(1fvd7)', 100) == 'Copy of something(1fvd7) (2)'