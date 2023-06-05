from functions.level_1.one_gender import genderalize


def test_genderalize_verb_male():
    assert genderalize("verb_male", "VF", "male") == "verb_male"

def test_genderalize_verb_female():
    assert genderalize("verb_male", "verb_female", "female") == "verb_female"

def test_genderalize_gender_else():
    assert genderalize("verb_male", "verb_female", '254654') == "verb_female"


