from functions.level_1.one_gender import genderalize


def test__genderalize__male_verb():
    assert genderalize("пошел", "пошла", 'male') == "пошел"


def test__genderalize__femaile_verb():
    assert genderalize("пошел", "пошла", 'female') == "пошла"


def test__genderalize__verb_of_uncertain_gender():
    assert genderalize("пошел", "пошла", 'uncertain') == "пошла"
