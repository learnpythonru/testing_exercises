from functions.level_1.three_url_builder import build_url
import pytest


@pytest.mark.parametrize(
    "host_name, relative_url, get_params, expected_result",
[
    ('host_name', 'relative_url', None, 'host_name/relative_url'),
    ('str1', 'relative_url', {'k': 'k_str', 'v': 'v_str'}, 'str1/relative_url?k=k_str&v=v_str'),
    ('host_name', 'relative_url', {'k': 'k_str'}, 'host_name/relative_url?k=k_str'),
    ('host_name', 'relative_url', {}, 'host_name/relative_url'),
]
)
def test__build_url__is_valid(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result


def test__build_url_only_host_name_typeerror():
    with pytest.raises(TypeError):
        build_url('host_name')
        

def test_build_url_only_get_params_typeerror():
    with pytest.raises(TypeError):
        build_url({'k': 'k_str'})


def test__build_url_value_error_no_parmeters():
    with pytest.raises(TypeError):
        build_url()


def test__build_url_bad_key_in_get_params_typeerror():
    with pytest.raises(TypeError):
        build_url('host_name', 'relative_url', {[1,1]: None})


def test__build_url_bad_key_in_get_params_attributeerror():
    with pytest.raises(AttributeError):
        build_url('host_name', 'relative_url', [1,1])