import pytest

from functions.level_1.five_title import change_copy_item


@pytest.fixture
def base_book():
    return 'Some book name (1234)', 20


@pytest.fixture
def base_copy_book(base_book):
    return 'Copy of '+ base_book[0], 100


def test_change_copy_item(base_book: tuple[str, int]):
    assert change_copy_item(base_book[0],
                            base_book[1]) == 'Some book name (1234)'


def test_change_copy_long_item(base_book):
    assert change_copy_item(base_book[0], 100) == 'Copy of Some book name (1234)'


def test_change_copy_item_number(base_copy_book: tuple[str, int]):
    assert change_copy_item(base_copy_book[0], base_copy_book[1]) ==\
           'Copy of Some book name (1235)'