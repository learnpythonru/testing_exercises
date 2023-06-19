from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize(
        'title, max_main_item_title_length, expected_result',
        [
            (
                'Hello World!',
                20,
                'Hello World!',
            ),
            (
                'Hello World!',
                100,
                'Copy of Hello World!',
            ),
            (
                'Copy of Hello World! (3)',
                100,
                'Copy of Hello World! (4)',
            ),
        ],
)
def test__change_copy_item__success(title, max_main_item_title_length, expected_result):
    assert change_copy_item(title, max_main_item_title_length) == expected_result


def test__change_copy_item__exception():
    with pytest.raises(AttributeError):
        change_copy_item(123, 100)
