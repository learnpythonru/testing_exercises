from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('Ivan', '123') == 'Ivan/123'
    assert build_url('Ivan', '123', {1: 45}) == 'Ivan/123?1=45'
    assert build_url('Ivan', '123', {1: 45, 2: 46}) == 'Ivan/123?1=45&2=46'
    assert build_url('Ivan', '123', {}) == 'Ivan/123'
