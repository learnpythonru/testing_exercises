from functions.level_1_5.three_first import first
import pytest

@pytest.mark.parametrize(
    "items,default,expected_result",
    [
        ([1, 2, 3], 1, 1),
        ([1, 2, 3], '', 1),
        ([], 1, 1),
    ],
    ids=["return_first_element_of_not_empty_items_when_defaul_int",
         "return_first_element_of_not_empty_items_when_defaul_is_None",
         "return_default_value_for_empty_items_and_default_is_int",
         ]
)
def test_first(items, default, expected_result):
    assert first(items, default) == expected_result


def test__first__items_is_None_and_default_not_set_return_exception():

    with pytest.raises(AttributeError):
        assert first(items=[])
