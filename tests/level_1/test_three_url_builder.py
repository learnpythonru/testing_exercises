from functions.level_1.three_url_builder import build_url


def test__build_url__with_parametrs():
    assert build_url("google.com", "search", {"q": "python"}) == "google.com/search?q=python"


def test__build_url__without_parametrs():
    assert build_url("google.com", "search") == "google.com/search"
