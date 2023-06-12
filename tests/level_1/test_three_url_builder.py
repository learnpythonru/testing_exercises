from functions.level_1.three_url_builder import build_url
import pytest


@pytest.mark.parametrize(
    'host_name, relative_url, get_params, expected_result',
    [
        (
            'https://yandex.ru',
            'search/',
            {
                'text': 'kinopoisk',
                'search_source': 'yaru_desktop_common',
                'src': 'suggest_Pers',
            },
            'https://yandex.ru/search/?text=kinopoisk&search_source=yaru_desktop_common&src=suggest_Pers',
        ),
        (
            'https://yandex.ru',
            'search/',
            None,
            'https://yandex.ru/search/',

        ),
        (
            'https://yandex.ru',
            'search/',
            {},
            'https://yandex.ru/search/',
        ),
    ],
)
def test__build_url(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result
