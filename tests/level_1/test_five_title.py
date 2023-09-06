from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize(
    'title,expected',
    [
        ("Hamlet", 'Copy of Hamlet'),
        ("Hamlet (105)", 'Copy of Hamlet (105)'),
        ("Copy of Hamlet (105)", 'Copy of Hamlet (106)'),
        ("Copy of Hamlet (-10)", 'Copy of Hamlet (-10) (2)'),
        ("Copy of Hamlet (by William Shakespeare)", 'Copy of Hamlet (by William Shakespeare) (2)'),
        ("", 'Copy of '),
    ]
)
def test_change_copy_item(title, expected):
    assert change_copy_item(title) == expected


@pytest.mark.parametrize(
    'title,main_item_title_length,expected',
    [
        ("Hamlet", 5, 'Hamlet'),
        ("Hamlet (105)", 5, 'Hamlet (105)'),
        ("Hamlet", 15, 'Copy of Hamlet'),
    ]
)
def test_change_copy_item_with_max_main_item_title_length(title, main_item_title_length, expected):
    assert change_copy_item(title, main_item_title_length) == expected


def test_change_copy_item_with_wrong_max_main_item_title_length():
    with pytest.raises(TypeError):
        change_copy_item("Hamlet", 'two')

def test_change_copy_item_with_wrong_title():
    with pytest.raises(AttributeError):
        change_copy_item(10)
