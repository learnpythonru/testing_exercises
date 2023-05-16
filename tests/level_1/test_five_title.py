import re
from functions.level_1.five_title import change_copy_item


def test_change_copy_item_():
    assert change_copy_item("123456789123456789qw") == "123456789123456789qw"
    assert change_copy_item("Hi") == "Copy of Hi"
    assert change_copy_item("Copy of Hallou") == "Copy of Hallou"
    assert change_copy_item("Copy of Hallou (3)") == "Copy of Hallou (3)"