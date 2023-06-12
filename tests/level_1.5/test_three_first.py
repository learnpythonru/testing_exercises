from functions.level_1_5.three_first import first
import pytest


@pytest.mark.parametrize(
        'items, default, expected_result',
        [
            ([1, 2, 3, 4], None, 1),
            ([], None, AttributeError),
            (['88', '2', '3', '4'], None, '88'),
            ([], 'def', 'def'),
            ([], (1, 5), (1, 5)),
            ({'a': 'b'}, None, KeyError),
        ],
)
def test__first(items, default, expected_result):
    if expected_result == AttributeError:
        with pytest.raises(AttributeError):
            first(items)
    elif expected_result == KeyError:
        with pytest.raises(KeyError):
            first(items)
    else:
        assert first(items, default) == expected_result
