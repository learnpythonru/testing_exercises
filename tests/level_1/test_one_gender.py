from functions.level_1.one_gender import genderalize
import pytest

@pytest.mark.parametrize(
        "verb_male,verb_female,gender,expected_result",
        [
            ("пошел", "пошла", "male", "пошел"),
            ("пошел", "пошла", "female", "пошла"),
            ("пошел", "пошла", "uncertain", "пошла"),
        ],
        ids=[
            "male verb",
            "female verb",
            "female verb returned for uncertain gender",
        ]
)
def test__genderalize__successfull(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) is expected_result
