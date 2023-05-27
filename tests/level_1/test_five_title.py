import re
from functions.level_1.five_title import change_copy_item


def test__change_copy_item__max_lenght_of_name():
    assert change_copy_item("123", 1) == "123"


def test__change_copy_item__add_copy_of():
    assert change_copy_item("Hi") == "Copy of Hi"


def test__change_copy_item__add_number_to_title():
    assert change_copy_item("Copy of Hallou") == "Copy of Hallou (2)"


def test__change_copy_item__increase_number_of_copies():
    assert change_copy_item("Copy of Hallou (3)") == "Copy of Hallou (4)"
