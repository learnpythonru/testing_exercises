from functions.level_1.one_gender import genderalize
import pytest


def test__genderalize__gender_is_male():
    assert genderalize("verb_male", "VF", "male") == "verb_male"


def test__genderalize__gender_is_female():
    assert genderalize("verb_male", "verb_female", "female") == "verb_female"


def test__genderalize__gender_is_other():
    assert genderalize("verb_male", "verb_female", '254654') == "verb_female"


def test__genderalize_only_two_parameters_typeerror():
    with pytest.raises(TypeError):
        genderalize("verb_male", "verb_female")