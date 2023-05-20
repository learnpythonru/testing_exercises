from functions.level_1.three_url_builder import build_url


def test_build_url():
    result = build_url("example.com", "path/to/resource")
    expected = "example.com/path/to/resource"
    assert result == expected

    result = build_url("example.com", "path/to/resource", {"param1": "value1", "param2": "value2"})
    expected = "example.com/path/to/resource?param1=value1&param2=value2"
    assert result == expected

    result = build_url("example.com", "path", {})
    expected = "example.com/path"
    assert result == expected