from functions.one_gender import genderalize
import pytest


@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected_result',
    [
        (pytest.lazy_fixture('male_verb'), pytest.lazy_fixture('female_verb'), 'male', pytest.lazy_fixture('male_verb')),
        (pytest.lazy_fixture('male_verb'), pytest.lazy_fixture('female_verb'), 'female', pytest.lazy_fixture('female_verb')),       
    ]
)
def test_genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result
