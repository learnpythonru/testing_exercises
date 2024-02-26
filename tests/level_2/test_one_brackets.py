from functions.level_2.one_brackets import delete_remove_brackets_quotes
import pytest



def test__delete_remove_brackets_quotes__function_in_return_of_result(name, result1):
    assert delete_remove_brackets_quotes(name) == result1

def test__delete_remove_brackets_quotes__result2_is_string(name, result2):
    assert delete_remove_brackets_quotes(name) == result2

# Вопрос:
# Похоже, мне нужны примеры грамотного использования фикстур в параметрайзах.
# Применила самый очевидный мне вариант в комментах ниже:
# Параметрайз здесь не видит файл конфтест.
# А если переношу фикстуры в текущий файл, жалуется, что name - это функция, 
# над которой нельзя производить действия как со строкой

#@pytest.mark.parametrize(
#    "name, expected_result",
#    [
#        (name, result1),
#        (name, result2),
#    ]
#)
#def test__delete_remove_brackets_quotes__is_valid(name, expected_result):
#    assert delete_remove_brackets_quotes(name) == expected_result