from functions.level_1.three_url_builder import build_url
import pytest

def test__build_url__two_parameters():
    assert build_url('host_name', 'relative_url') ==  'host_name/relative_url'


def test__build_url__get_parameters():
    get_params = {'k': 'k_str', 'v': 'v_str'}
    assert build_url('str1', 'relative_url', get_params) == 'str1/relative_url?k=k_str&v=v_str'


def test__build_url__get_parameters_short():
    assert build_url('host_name', 'relative_url', {'k': 'k_str'}) == 'host_name/relative_url?k=k_str'


def tesr__build_url__get_parameters_empty():
    assert build_url('host_name', 'relative_url', {}) == 'host_name/relative_url'


def test__three__value_error_only_host_name():
    with pytest.raises(TypeError):
        build_url('host_name')
        

def test_three_value_error_only_get_params():
    with pytest.raises(TypeError):
        build_url({'k': 'k_str'})

def test_three_value_error_no_parmeters():
    with pytest.raises(TypeError):
        build_url()

def test__three__value_error_bad_key_in_get_params():
    with pytest.raises(TypeError):
        build_url('host_name', 'relative_url', {[1,1]: None})

def test__three__value_error_bad_key_in_get_params():
    with pytest.raises(AttributeError):
        build_url('host_name', 'relative_url', [1,1])