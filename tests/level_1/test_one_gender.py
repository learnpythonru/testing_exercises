from functions.level_1.one_gender import genderalize


def test_genderalize():
    verb_male = "VM"
    verb_female="VF"
    gender_male = "male"
    gender_else = "female"
    assert genderalize(verb_male, verb_female, gender_male) == verb_male
    assert genderalize(verb_male, verb_female, gender_else) == verb_female
    assert not genderalize(verb_male, verb_female, gender_else) == verb_male
    assert not genderalize(verb_male, verb_female, gender_male) == verb_female
    assert genderalize(verb_male, verb_female, '254654') == verb_female


def test_genderalize_type():
    verb_male = "VM"
    verb_female="VF"
    gender_male = "male"
    gender_else = "female"
    assert type(genderalize(verb_male, verb_female, gender_male)) == str