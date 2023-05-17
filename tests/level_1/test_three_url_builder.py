from functions.level_1.three_url_builder import build_url
import pytest

def test_build_url_two_parameters():
    assert build_url('host_name', 'relative_url') ==  'host_name/relative_url'


def test_build_url_get_parameters():
    get_params = {'k': 'k_str', 'v': 'v_str'}
    assert build_url('str1', 'relative_url', get_params) == 'str1/relative_url?k=k_str&v=v_str'


def test_three_value_error():
    with pytest.raises(ValueError, match="ValueError"):
        raise ValueError("ValueError!!!")
        build_url(["202yhbmj5", 1], 14645)
        build_url({'fere': 0}, 134, "Python", 1,2,3 )
        build_url(1, {"32":21, '323':1}, 0)