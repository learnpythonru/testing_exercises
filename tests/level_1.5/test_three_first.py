from functions.level_1_5.three_first import first
import pytest


@pytest.mark.parametrize(
    'items, default, expected_result',
    [
        ([1, 2, 3, 4], None, 1),
        (['88', '2', '3', '4'], None, '88'),
        ([], 'def', 'def'),
        ([], (1, 5), (1, 5)),
    ],
)
def test__first__success(items, default, expected_result):
    assert first(items, default) == expected_result


@pytest.mark.parametrize(
    'items, default, exception_type',
    [
        ([], None, AttributeError),
        ({'a': 'b'}, None, KeyError),
    ],
)
def test__first__exceptions(items, default, exception_type):
    with pytest.raises(exception_type):
        first(items)
