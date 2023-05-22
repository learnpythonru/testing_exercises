from functions.level_1.one_gender import genderalize


def test__genderalize__male():
    assert genderalize('сказал', 'сказала', 'male') == 'сказал'


def test__genderalize__male():
    assert genderalize('сказал', 'сказала', 'female') == 'сказала'