import pytest

from faker import Faker
from functions.five_title import change_copy_item

fake = Faker()

long_title = fake.text()
short_title = fake.text(max_nb_chars=30)


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected",
    [
        (long_title, 100, long_title),
        (f"{long_title} (9)", 50, f"{long_title} (9)"),
        (short_title, 100, f"Copy of {short_title}"),
        (f"Copy of {short_title} (5)", 100, f"Copy of {short_title} (6)"),
    ],
)
def test_change_copy_item(title: str, max_main_item_title_length: int, expected: str):
    assert change_copy_item(title, max_main_item_title_length) == expected
