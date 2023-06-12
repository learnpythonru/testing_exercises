from functions.level_1_5.three_first import first
import pytest


@pytest.mark.parametrize(
  "items, default, expected_result, items_need",
  [
      ('items_1', 'default_1', 'result_1', True),
      ('items_1', 'default_2', 'result_1', True),
      ('items_2', 'default_3', 'default_3', True),
      ('items_3', 'default_3', 'default_3', True),
      ('items_4', 'default_3', 'default_3', True),
      ('items_4', 'default_4', 'default_4', True),
      ('items_4', 'default_1', 'default_1', True ),
      ('items_4', 'default_5', 'default_5', True),
      ('items_5', 'default_3', 'result_5', False),
      ('items_5', 'default_2', 'result_6', False)
  ]      
)
def test__first__is_valid(items, default, expected_result, items_need, request):
    items = request.getfixturevalue(items)
    default = request.getfixturevalue(default)
    expected_result = request.getfixturevalue(expected_result)
    if items_need:
        assert first(items, default) is expected_result
    else:
        assert first(default) is expected_result

@pytest.mark.parametrize(
  "items, default, expected_error, items_need, default_need",
  [
      ('items_2', 'default_6', AttributeError, True, False),
      ('items_2', 'default_2', AttributeError, True, True),
      ('items_5', 'default_6', TypeError, False, False),
  ]      
)
def test__first__errors(items, default, expected_error, items_need, default_need, request):  
    items = request.getfixturevalue(items)
    default = request.getfixturevalue(default)
    with pytest.raises(expected_error):
        if items_need:
            if default_need:
                first(items, default)
            else:
                first(items)
        else:
            if default_need:
                pass
            else:
                first()


def test__first__items_is_empty_attributeerror():  
    with pytest.raises(AttributeError):  
        first([], )
