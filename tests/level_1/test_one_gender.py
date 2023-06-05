from functions.level_1.one_gender import genderalize
import pytest


def test__genderalize__is_male():
    assert genderalize('говорил', 'говорила', 'male') == 'говорил'

def test__genderalize__is_not_male():
    assert genderalize('говорил', 'говорила', 'any str, except "male"') == 'говорила'

@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected_result',
    [
        ('говорил', 'говорила', 'male', 'говорил'),
        ('говорил', 'говорила', 'any str, except "male', 'говорила'),
    ]
)
def test__genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result