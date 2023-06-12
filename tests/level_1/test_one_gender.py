from functions.level_1.one_gender import genderalize
import pytest
import datetime


# Капец я долго с этим разбиралась. 
# Есть впечатление, что в гугле недостаточно структурной инфы на эту тему.
# Только спустя несколько дней нашла норм ресурс, где доступно описывается добавление параметра request
# https://engineeringfordatascience.com/posts/pytest_fixtures_with_parameterize/

# Комменты оставляю и для себя, и для тебя, чтобы ты подтвердил, что я поняла всю логику верно)


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


# Вопрос: уместно ли делать папаметрайзы для одного-единственного кейса,
# если вотпрямщаз вроде вариант для теста только один, 
# но есть планы на доработку функции и ты заранее знаешь, что скоро вариантов станет больше?

# Конкретно здесь оставляю этот один вариант, чисто тобы в том же коде, никуда не листая, пощупать параметрайз эрроров :)
@pytest.mark.parametrize('VM, VF,  expected_error_genderalize', 
                         [
 #                            ('verb_male', 'verb_female', TypeError),
                             ('verb_male', 'verb_female', 'type_error') #ВОПРОС: с эррорами как правильнее, 
                                                                        # выносить в отдельную фикстуру или оставлять как в строке выше?
                         ]
                        )
def test__genderalize_only_two_parameters_typeerror(VM, VF, expected_error_genderalize, request):
    VM = request.getfixturevalue(VM)
    VF = request.getfixturevalue(VF)
    expected_error_genderalize = request.getfixturevalue(expected_error_genderalize)
    with pytest.raises(expected_error_genderalize):
       genderalize(VM, VF)


