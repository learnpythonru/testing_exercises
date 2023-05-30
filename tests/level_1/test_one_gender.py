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
            "mail_verb",
            "femail_verb",
            "verb_of_uncertain_gender",
        ]
)
def test__genderalize__input_three_types_of_verbs(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) is expected_result
