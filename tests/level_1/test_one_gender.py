from functions.level_1.one_gender import genderalize
import pytest



#  норм ресурс, где доступно описывается добавление параметра request
# https://engineeringfordatascience.com/posts/pytest_fixtures_with_parameterize/

@pytest.mark.parametrize('VM, VF, gender,  expected_result_genderalize', #просто переменные
                         [('verb_male', 'verb_female', 'gender_male', 'verb_male'), # названия фикстур
                          ('verb_male', 'verb_female', 'gender_female','verb_female'),
                          ('verb_male', 'verb_female', 'random_symbols','verb_female')
                         ]
                        )
def test__genderalize__is_valid(VM, VF, gender, expected_result_genderalize, request):
    VM = request.getfixturevalue(VM) # вытащить из фикстуры значение, которое она возвращает
    VF = request.getfixturevalue(VF)
    gender = request.getfixturevalue(gender)
    expected_result_genderalize_ = request.getfixturevalue(expected_result_genderalize)
    assert genderalize(VM, VF, gender) == expected_result_genderalize


@pytest.mark.parametrize('vm, vf,  expected_error_genderalize', 
                         [
                             ('verb_male', 'verb_female', TypeError),
                         ]
                        )
def test__genderalize_only_two_parameters_typeerror(vm, vf, expected_error_genderalize, request):
    vm = request.getfixturevalue(vm)
    vf = request.getfixturevalue(vf)
    with pytest.raises(expected_error_genderalize):
       genderalize(vm, vf)


