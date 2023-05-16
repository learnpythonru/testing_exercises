from functions.level_1.one_gender import genderalize


def test_genderalize_verb_male():
    # Вопрос 1: теперь не создаю переменные verb_male = "VM", gender_male = "male" и тд
    # в тестах без них просто можно, или ещё и нужно?
    # имхо без переменных неудобно
    assert genderalize("verb_male", "VF", "male") == "verb_male"

def test_genderalize_verb_female():
    assert genderalize("verb_male", "verb_female", "female") == "verb_female"

def test_genderalize_gender_else():
    assert genderalize("verb_male", "verb_female", '254654') == "verb_female"


# Вопрос 2 (хотя после теории по mypy уже догадываюсь): 
# надо ли в тестах проверять типы?
# Догадываюсь, что не надо, и что май пай берёт на себя всю эту нагрузку
# убрала соответствующую функцию
