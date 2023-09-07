from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('получил', 'получила', 'male') == 'получил'
    assert genderalize('получил', 'получила', 'female') == 'получила'
    

