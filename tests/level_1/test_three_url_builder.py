from functions.level_1.three_url_builder import build_url
import pytest


@pytest.mark.parametrize(
    "host_name,relative_url,get_params,expected_result",
    [
        ("google.com", "search", {"q": "python"}, "google.com/search?q=python"),
        ("google.com", "search", "", "google.com/search"),
    ],
    ids=[
     "with params",
     "without params"
    ]
)
def test_build_url__succsessfull(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result
