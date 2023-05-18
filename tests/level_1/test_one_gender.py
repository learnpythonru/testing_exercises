from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('сказал', 'сказала', "male") == 'сказал'    
    assert not genderalize('сказал', 'сказала', "male") == 'сказала'