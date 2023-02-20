import pytest

from functions.one_gender import genderalize

verb_male = "Делал"
verb_female_value = "Делала"


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected",
    [
        (verb_male, verb_female_value, "male", verb_male),
        (verb_male, verb_female_value, "female", verb_female_value),
    ],
)
def test_genderalize(verb_male: str, verb_female: str, gender: str, expected: str):
    assert genderalize(verb_male, verb_female, gender) == expected
