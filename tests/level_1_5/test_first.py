from functions.level_1_5.three_first import first, NOT_SET
import pytest


@pytest.mark.parametrize(
  "items, default, expected_result",
  [
      ([1, 2, 3], None, 1),
      ([1, 2, 3], NOT_SET, 1),
      ([], 'default', 'default'),
      ('', 'default', 'default'),
      (None, 'default', 'default'),
      (None, 1234, 1234),
      (None, None, None),
      (None, (5, 56), (5, 56)),
  ]      
)

def test__first__is_valid(items, default, expected_result):
    assert first(items, default) is expected_result


# ВОПРОС: как параметризовать такие варианты, 
# когда один из параметров не передаётся?
# Через None?
def test__first__defaults_is_string():
    assert first('default') == 'd'

 
def test__first__defaults_is_not_set():   
    assert first(NOT_SET) == 'N'


def test__first__items_is_empty_no_defaults_attributeerror():  
    with pytest.raises(AttributeError):
        first([])


def test__first__items_is_empty_attributeerror():  
    with pytest.raises(AttributeError):  
        first([], NOT_SET)


def test__first__no_parameters():  
    with pytest.raises(TypeError):
        first()