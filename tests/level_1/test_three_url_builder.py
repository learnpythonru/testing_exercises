import pytest
from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize("input_host,input_url,input_params,expected", [
    ("google.com", "search", {"q": "python"}, "google.com/search?q=python"), 
    ("google.com", "search", "", "google.com/search")])
def test__build_url__with_or_without_params(input_host, input_url, input_params, expected):
    assert build_url(input_host, input_url, input_params) == expected
