from functions.level_1_5.one_median import get_median_value
import pytest

def test__get_median_value__return_None_when_no_inputed_values():
    items = []
    assert get_median_value(items) is None

@pytest.mark.parametrize(
        "items,expected_result",
        [
            pytest.param([11, 9, 3, 5, 7], 7, marks=pytest.mark.xfail(reason='incorrect result for odd numbers of arguments')),
            pytest.param([1, 3, 5, 7], 4, marks=pytest.mark.xfail(reason='incorrect result for even numbers of arguments')),
        ],
        ids=[
            "odd number of values",
            "even number of values less then 6",
        ]
)
def test__get_median_value__fail_return_incorrect_value_due_to_misstake_in_func(items, expected_result):
    assert get_median_value(items) == expected_result


@pytest.mark.parametrize(
        "items,expected_result",
        [
            ([11, 9, 3, 5, 7, 6], 6),
            ([11, 9, 3, 5, 7, 6, 12, 15], 9),
        ]
)
def test__get_median_value__succcess_when_even_number_of_values_6_or_more(items, expected_result):
    assert get_median_value(items) == expected_result
