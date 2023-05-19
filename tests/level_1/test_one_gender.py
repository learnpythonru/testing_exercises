from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('Ходил', 'Ходила', 'male') == 'Ходил'
    assert genderalize('Ходил', 'Ходила', 'female') == 'Ходила'
    assert genderalize('Ходил', 'Ходила', 'banana') == 'Ходила'
