from functions.level_1_5.one_median import get_median_value
import pytest

def test__get_median_value_empty_params():
    items = ''
    get_median_value_result = get_median_value(items)
    assert get_median_value_result == None


def test__get_median_value_list_of_three_params():
    items = [2,1,5]
    get_median_value_result = get_median_value(items)
    assert get_median_value_result == 5


def test__get_median_value_list_of_negative_values():
    items = [-2,-1,5]
    get_median_value_result = get_median_value(items)
    assert get_median_value_result == 5


def test__get_median_value_list_of_odd_params():
    items = [2,1,3,9, 10]
    get_median_value_result = get_median_value(items)
    assert get_median_value_result == 9


def test__get_median_value_list_of_even_params():
    items = [2,1,1,1,3,3,2,9,9,3,9, 10]
    get_median_value_result = get_median_value(items)
    assert get_median_value_result == 9


def test__get_median_value_list_of_float_params():
    items = [0.6, 99.4, 13.2]
    get_median_value_result = get_median_value(items)
    assert get_median_value([0.6, 99.4, 13.2])==13.2

# Вопрос: а как наложить принцип ААА на проверкутаких ошибок?
def test__get_median_value_no_params_typeerror():
        with pytest.raises(TypeError):
            get_median_value()


def test__get_median_list_of_four_params_indexerror():
        with pytest.raises(IndexError):
            get_median_value([2,1,3,9])


def test__get_median_one_int_in_params_typeerror():
        with pytest.raises(TypeError):
            get_median_value(1)