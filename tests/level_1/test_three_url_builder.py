from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url("google.com","search", {"q": "python"}) == "google.com/search?q=python"
    assert build_url("google.com","search") == "google.com/search"