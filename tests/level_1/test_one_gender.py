from functions.level_1.one_gender import genderalize


def test__genderalize__male():
    assert genderalize('Ходил', 'Ходила', 'male') == 'Ходил'
def test__genderalize__female():
    assert genderalize('Ходил', 'Ходила', 'female') == 'Ходила'
def test__genderalize__something_else():
    assert genderalize('Ходил', 'Ходила', 'banana') == 'Ходила'
