from functions.level_1_5.three_first import first, NOT_SET
import pytest


@pytest.mark.parametrize(
  "items, default, expected_result, items_need",
  [
      ([1, 2, 3], None, 1, 1),
      ([1, 2, 3], NOT_SET, 1, 1),
      ([], 'default', 'default', 1),
      ('', 'default', 'default', 1),
      (None, 'default', 'default', 1),
      (None, 1234, 1234, 1),
      (None, None, None, 1 ),
      (None, (5, 56), (5, 56), 1),
      (0, 'default', 'd', 0),
      (0, NOT_SET, 'N', 0)
  ]      
)
def test__first__is_valid(items, default, expected_result, items_need):
    if items_need == 1:
        assert first(items, default) is expected_result
    else:
        assert first(default) is expected_result

@pytest.mark.parametrize(
  "items, default, expected_error, items_need, default_need",
  [
      ([], 0, AttributeError, 1, 0),
      ([], NOT_SET, AttributeError, 1, 1),
      (0, 0, TypeError, 0, 0),
  ]      
)
def test__first__errors(items, default, expected_error, items_need, default_need):  
    with pytest.raises(expected_error):
        if items_need == 1:
            if default_need == 1:
                first(items, default)
            else:
                first(items)
        else:
            if default_need == 1:
                pass
            else:
                first()


def test__first__items_is_empty_attributeerror():  
    with pytest.raises(AttributeError):  
        first([], )
