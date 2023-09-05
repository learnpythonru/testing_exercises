from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url("https://confluence.hz.ru/", "pages/viewpage.action", {'pageId': '7569538209'}) == "https://confluence.hz.ru//pages/viewpage.action?pageId=7569538209"
