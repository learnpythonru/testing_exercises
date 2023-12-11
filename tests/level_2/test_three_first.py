import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize('items, default, expected_result', [
    ([1, 2, 3], None, 1),
    ([1, 2, 3], 'NOT_SET', 1),
    ([1, 2, 3], 8, 1),
    ([], 5, 5),
    (None, 6, 6),
    (None, None, None),
])
def test__first__succes(items, default, expected_result):
    assert first(items=items, default=default) == expected_result


@pytest.mark.parametrize('items, default', [
    ([], 'NOT_SET'),
    (None, 'NOT_SET')
])
def test__first__with_atribute_error(items, default):
    with pytest.raises(AttributeError):
        first(items=items, default=default)
