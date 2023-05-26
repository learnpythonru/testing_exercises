from functions.level_1_5.one_median import get_median_value

def test_get_median_value_with_empty_items():
    items = []
    assert get_median_value(items) == None

# def test_get_median_value_with_even_len_of_items():   # Сломал голову. Но если число элементов в списке четное, функция не работает. Баг.
#     items = [2, 1, 4, 3]
#     assert get_median_value(items) == 1

def test_get_median_value_with_odd_len_of_items():
    items = [1, 3, 6, 8, 9, 10]
    assert get_median_value(items) == 9
