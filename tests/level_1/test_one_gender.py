from functions.level_1.one_gender import genderalize


def test_genderalize_is_male():
    assert genderalize('говорил', 'говорила', 'male') == 'говорил'

def test_genderalize_is_not_male():
    assert genderalize('говорил', 'говорила', 'any str, except "male"') == 'говорила'

