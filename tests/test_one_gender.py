import pytest

from functions.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected",
    [
        (
            pytest.lazy_fixture("verb_male_value"),
            pytest.lazy_fixture("verb_female_value"),
            "male",
            pytest.lazy_fixture("verb_male_value"),
        ),
        (
            pytest.lazy_fixture("verb_male_value"),
            pytest.lazy_fixture("verb_female_value"),
            "female",
            pytest.lazy_fixture("verb_female_value"),
        ),
    ],
)
def test_genderalize(verb_male: str, verb_female: str, gender: str, expected: str):
    assert genderalize(verb_male, verb_female, gender) == expected
