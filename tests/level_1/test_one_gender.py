from functions.level_1.one_gender import genderalize
import pytest


@pytest.fixture
def verb_male():
    return "verb_male"

@pytest.fixture
def verb_female():
    return "verb_female"

@pytest.fixture
def random_symbols():
    return "4w5rgt"

@pytest.mark.parametrize(
  "verb_male, verb_female, gender, expected_result",
  [
      (verb_male, random_symbols, "male", verb_male),
      (verb_male, verb_female, "female", verb_female),
      (verb_male, verb_female, random_symbols, verb_female),
  ]      
)
def test__genderalize__is_valid(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result


def test__genderalize_only_two_parameters_typeerror():
    with pytest.raises(TypeError):
        genderalize(verb_male, verb_female)
