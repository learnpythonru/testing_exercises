from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('https://yandex.ru', 'search/', {'text':'kinopoisk',
                                                       'search_source' : 'yaru_desktop_common',
                                                       'src' : 'suggest_Pers'}) == 'https://yandex.ru/search/?text=kinopoisk&search_source=yaru_desktop_common&src=suggest_Pers'
    