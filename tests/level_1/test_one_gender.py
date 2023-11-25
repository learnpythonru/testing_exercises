import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize('verb_male, verb_female, gender, expected_result', [
    ('Красивый', 'Красивая', 'male', 'Красивый'),
    ('Спортивный', 'Спортивная', 'female', 'Спортивная'),
    ('Активный', 'Активная', 'unknown', 'Активная'),
])
def test_genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male=verb_male, verb_female=verb_female,
                       gender=gender) == expected_result
