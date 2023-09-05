from functions.level_1.one_gender import genderalize


def test_genderalize():
    # verb_male if gender == "male" else verb_female
    assert genderalize('otec', 'mat', 'male') == 'otec'
