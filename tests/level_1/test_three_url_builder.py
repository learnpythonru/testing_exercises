import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
        'host_name, relative_url, get_params, expected_result', [
            ('example.com', 'search', {'language': 'RU'},
             'example.com/search?language=RU'),
            ('localhost', 'api', None, 'localhost/api'),
            ('test.ru', 'some_path', {
                'key1': '1',
                'key2': '2',
                'key3': '3',
            },
             'test.ru/some_path?key1=1&key2=2&key3=3')
        ])
def test_build_url(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name=host_name, relative_url=relative_url,
                     get_params=get_params) == expected_result
