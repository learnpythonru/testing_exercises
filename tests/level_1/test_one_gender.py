from functions.level_1.one_gender import genderalize


def test__genderalize__male():
    gender = 'male'

    result = genderalize('сказал', 'сказала', gender)

    assert result == 'сказал'


def test__genderalize__male():
    gender = 'female'

    result = genderalize('сказал', 'сказала', gender)

    assert result == 'сказала'