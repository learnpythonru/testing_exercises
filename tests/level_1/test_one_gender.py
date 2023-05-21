from functions.level_1.one_gender import genderalize


def test__genderalize__male():
    gender = 'male'

    assert genderalize('сказал', 'сказала', gender) == 'сказал'


def test__genderalize__male():
    gender = 'female'

    assert genderalize('сказал', 'сказала', gender) == 'сказала'