from functions.level_1.three_url_builder import build_url


def test_build_url():
    get_params = {'k': 'k_str', 'v': 'v_str'}
    assert build_url('host_name', 'relative_url') ==  'host_name/relative_url'
    assert build_url('str1', 'relative_url', get_params) == 'str1/relative_url?k=k_str&v=v_str'
