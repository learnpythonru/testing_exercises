from functions.level_1_5.one_median import get_median_value
import pytest



@pytest.mark.parametrize(
  "items, expected_result",
  [
      ('', None),
      ([2, 1, 5], 5),
      ([-2, -1, 5], 5),
      ([2, 1, 3, 9, 10], 9),
      ([2, 1, 1, 1, 3, 3, 2, 9, 9, 3, 9, 10], 9),
      ([0.6, 99.4, 13.2],  13.2),
  ]      
)
def test__get_median__is_valid(items, expected_result):
    assert get_median_value(items) is expected_result

@pytest.mark.parametrize(
  "items, expected_error, items_need",
  [
       (0, TypeError, 0),
       ([2, 1, 3, 9], IndexError, 1),
       (1, TypeError, 1),
  ]
)
def test__get_median_value__errors(items, expected_error, items_need):
    with pytest.raises(expected_error):
        if items_need == 1:
            get_median_value(items)
        else:
            get_median_value()
