import pytest

from functions.five_title import change_copy_item


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected",
    [
        (
            pytest.lazy_fixture("long_title"),
            100,
            pytest.lazy_fixture("long_title"),
        ),
        (
            pytest.lazy_fixture("long_title_with_brackets"),
            50,
            pytest.lazy_fixture("long_title_with_brackets"),
        ),
        (
            pytest.lazy_fixture("short_title"),
            100,
            pytest.lazy_fixture("copy_of_short_title"),
        ),
        (
            pytest.lazy_fixture("short_title_with_brackets"),
            100,
            pytest.lazy_fixture("short_title_with_brackets_copy"),
        ),
    ],
)
def test_change_copy_item(title: str, max_main_item_title_length: int, expected: str):
    assert change_copy_item(title, max_main_item_title_length) == expected
