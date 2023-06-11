from functions.level_1.three_url_builder import build_url
import pytest




@pytest.mark.parametrize(
    "host_name, relative_url, get_params, expected_result",
[
    ('host_name_1', 'relative_url', 'get_params_none', 'url_no_querypart'),
    ('host_name_2', 'relative_url', 'get_params_mappings_k_and_v', 'url_k_and_v'),
    ('host_name_1', 'relative_url', 'get_params_mappings_k', 'url_k'),
    ('host_name_1', 'relative_url', 'get_params_no_querypart', 'url_no_querypart'),
]
)
def test__build_url__is_valid(host_name, relative_url, get_params, expected_result, request):
    host_name = request.getfixturevalue(host_name)
    relative_url = request.getfixturevalue(relative_url)
    get_params = request.getfixturevalue(get_params)
    expected_result = request.getfixturevalue(expected_result)
    assert build_url(host_name, relative_url, get_params) == expected_result


def test__build_url_only_host_name_typeerror(host_name_1):
    with pytest.raises(TypeError):
        build_url(host_name_1)
        

def test_build_url_only_get_params_typeerror(get_params_mappings_k):
    with pytest.raises(TypeError):
        build_url(get_params_mappings_k)


def test__build_url_value_error_no_parmeters():
    with pytest.raises(TypeError):
        build_url()

# хочу закоменченный вариант, но не знаю как его использовать без ошибок(
#def test__build_url_bad_key_in_get_params_typeerror(host_name_1, relative_url, get_params_error):
def test__build_url_bad_key_in_get_params_typeerror(host_name_1, relative_url):
    with pytest.raises(TypeError):
    #    build_url(host_name_1, relative_url, get_params_error)
        build_url(host_name_1, relative_url, {[1,1]: None})


def test__build_url_bad_key_in_get_params_attributeerror(host_name_1, relative_url, get_params_attr_error):
    with pytest.raises(AttributeError):
        build_url(host_name_1, relative_url, get_params_attr_error)