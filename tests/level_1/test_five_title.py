import pytest
from functions.level_1.five_title import change_copy_item


def test__change_copy_item__max_lenght_of_name():
    assert change_copy_item("123", 1) == "123"


@pytest.mark.parametrize(
        "title,expected_result",
        [
            ("Hi", "Copy of Hi"),
            ("Copy of Hallou", "Copy of Hallou (2)"),
            ("Copy of Hallou (3)", "Copy of Hallou (4)"),
        ],
        ids=[
            "add_text_copy_of",
            "add number to title",
            "increase number of copies"
        ]
)
def test_change_copy_item(title, expected_result):
    assert change_copy_item(title) == expected_result

