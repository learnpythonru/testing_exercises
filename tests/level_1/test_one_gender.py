from functions.level_1.one_gender import genderalize
import pytest



@pytest.mark.parametrize(
  "verb_male, verb_female, gender, expected_result",
  [
      ("verb_male", "VF", "male", "verb_male"),
      ("verb_male", "verb_female", "female", "verb_female"),
      ("verb_male", "verb_female", '254654', "verb_female"),
  ]      
)
def test__genderalize__is_valid(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) is expected_result


def test__genderalize_only_two_parameters_typeerror():
    with pytest.raises(TypeError):
        genderalize("verb_male", "verb_female")