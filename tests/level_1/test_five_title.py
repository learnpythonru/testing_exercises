import pytest
from functions.level_1.five_title import change_copy_item


def test__change_copy_item__max_lenght_of_name():
    assert change_copy_item("123", 1) == "123"

def test__change_copy_item__add_text_copy_of():
    assert change_copy_item("Hi") == "Copy of Hi"

@pytest.mark.parametrize(
        "title,expected_result",
        [
            ("Copy of Hallou", "Copy of Hallou (2)"),
            ("Copy of Hallou (3)", "Copy of Hallou (4)"),
        ]
)
def test_change_copy_item__add_copy_level_for_copy_of_copy(title, expected_result):
    assert change_copy_item(title) == expected_result

