from functions.level_1.three_url_builder import build_url


def test_build_url():
    host_name = 'https://yandex.ru'
    relative_url = 'search/'
    get_params = {'text':'kinopoisk',
        'search_source' : 'yaru_desktop_common',
        'src' : 'suggest_Pers',
    }
    exprcted_result = 'https://yandex.ru/search/?text=kinopoisk&search_source=yaru_desktop_common&src=suggest_Pers'

    result = build_url(host_name, relative_url, get_params)
    
    assert result == exprcted_result
    