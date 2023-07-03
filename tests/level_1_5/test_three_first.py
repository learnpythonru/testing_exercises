from functions.level_1_5.three_first import first
import pytest

@pytest.mark.parametrize(
    "items,default,expected_result",
    [
        ([1, 2, 3], 4, 1),
        ([1, 2, 3], '', 1),
    ],
    ids=["defaul_int",
         "defaul_is_None",
         ]
)
def test__first__success_return_first_element_of_not_empty_items(items, default, expected_result):
    assert first(items, default) == expected_result


@pytest.mark.parametrize(
    "items,default,expected_result",
    [
        ([], 1, 1),
        ([], 3, 3)
    ]
)
def test__first__success__return_default_value_for_empty_items_and_default_is_int(items, default, expected_result):
    assert first(items, default) == expected_result


def test__first__items_is_None_and_default_not_set_return_exception():
    with pytest.raises(AttributeError):
        assert first(items=[])
