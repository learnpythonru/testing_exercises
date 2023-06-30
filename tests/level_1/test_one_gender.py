import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
        'verb_male,verb_female,gender,expected_output',
        [
            ('Ходил', 'Ходила', 'male', 'Ходил'),
            ('Ходил', 'Ходила', 'female', 'Ходила'),
            ('Ходил', 'Ходила', 'banana', 'Ходила'),
        ],
        ids=[
            'Trying the male version',
            'Trying the female version',
            'Trying the any other str input version',
        ]
)
def test_genderalize(verb_male, verb_female, gender, expected_output):
    assert genderalize(verb_male, verb_female, gender) == expected_output
