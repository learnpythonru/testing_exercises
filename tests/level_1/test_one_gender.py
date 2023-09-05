from functions.level_1.one_gender import genderalize
import pytest


@pytest.mark.parametrize(
    "verb_male,verb_female,gender,expected",
    [
        ('сделал', 'сделала', 'male', 'сделал'),
        ('сделал', 'сделала', 'female', 'сделала'),
        (False, 'сделала', 'male', False),
        (0, 1, 10, 1),
    ])
def test_genderalize(verb_male, verb_female, gender, expected):
    assert genderalize(verb_male, verb_female, gender) == expected
