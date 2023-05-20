from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('говорил', 'говорила', 'male') == 'говорил'
    assert genderalize('говорил', 'говорила', 'female') == 'говорила'
    assert genderalize('говорил', 'говорила', 'transgender') == 'говорила'