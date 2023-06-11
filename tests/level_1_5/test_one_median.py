from functions.level_1_5.one_median import get_median_value
import pytest

@pytest.mark.parametrize(
        "items,expected_result",
        [
            ([], None),
            pytest.param([11, 9, 3, 5, 7], 7, marks=pytest.mark.xfail(reason='incorrect result for odd numbers of arguments')),
            pytest.param([1, 3, 5, 7], 4, marks=pytest.mark.xfail(reason='incorrect result for even numbers of arguments')),
            ([11, 9, 3, 5, 7, 6], 6),
        ],
        ids=[
            "no items return is none",
            "odd number",
            "even number less then 6",
            "even number is 6 and more",
        ]
)
def test__get_median_value__two_correct_returns_and_two_incorrect_due_to_misstake_in_func(items, expected_result):
    assert get_median_value(items) == expected_result
