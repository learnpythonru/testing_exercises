from functions.level_1_5.one_median import get_median_value
import pytest


@pytest.mark.parametrize(
    'items, expected_result',
    [
        ([], None),
        ([8, 1, 3, 2, 5, 7], 6),
        ([8, 1, 3, 2, 5], 2),
        ([8, 1, 3, 2], IndexError),
    ],
)
def test__get_median_value(items, expected_result):
    if expected_result == IndexError:
        with pytest.raises(IndexError):
            get_median_value(items)
    else:
        assert get_median_value(items) == expected_result
