from functions.level_1.one_gender import genderalize
import pytest


@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected_result',
    [
        ('сказал', 'сказала', 'male', 'сказал'),
        ('сказал', 'сказала', 'female', 'сказала'),
        ('сказал', 'сказала', 'none', 'сказала'),
    ],
)
def test__genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result
