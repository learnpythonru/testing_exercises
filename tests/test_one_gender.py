from functions.one_gender import genderalize
import pytest


@pytest.mark.parametrize(
    'gender, expected_result',
    [
        ('male', 'male_verb'),
        ('female', 'female_verb'),       
    ]
)
def test_genderalize(gender, expected_result):
    assert genderalize('male_verb', 'female_verb', gender) == expected_result
