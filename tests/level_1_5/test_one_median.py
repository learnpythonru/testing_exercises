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

def test__get_median_value__empty_params():
    assert get_median_value('') == None


def test__get_median_value__no_params_typeerror():
    with pytest.raises(TypeError):
        get_median_value()


def test__get_median_value__list_of_four_params_indexerror():
    with pytest.raises(IndexError):
        get_median_value([2, 1, 3, 9])


def test__get_median_value__one_int_in_params_typeerror():
        with pytest.raises(TypeError):
            get_median_value(1)