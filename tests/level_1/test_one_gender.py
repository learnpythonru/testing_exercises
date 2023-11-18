from functions.level_1.one_gender import genderalize
import pytest


@pytest.mark.parametrize('verb_male, verb_female, gender, expected_result', [
    ('Красивый', 'Красивая', 'male', 'Красивый'),
    ('Спортивный', 'Спортивная', 'female', 'Спортивная'),
    ('Активный', 'Активная', 'unknown', 'Активная'),
])
def test_genderalize(verb_male: str, verb_female: str, gender: str,
                     expected_result: str):
    assert genderalize(verb_male=verb_male, verb_female=verb_female,
                       gender=gender) == expected_result
