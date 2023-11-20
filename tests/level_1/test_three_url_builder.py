import pytest

from functions.level_1.three_url_builder import build_url


@pytest.fixture
def base_url_data():
    return 'some-url.com', 'relative_part'


@pytest.fixture
def url_data_params(base_url_data):
    return (base_url_data[0],
            base_url_data[1],
            {'param1': 'value1', 'param2': 'value2'})


def test_build_url(base_url_data):
    assert build_url(base_url_data[0],
                     base_url_data[1]) == 'some-url.com/relative_part'


def test_build_url_params(url_data_params: tuple[str, str, dict[str, str]]):
    assert build_url(url_data_params[0],
                     url_data_params[1],
                     url_data_params[2]) == \
           'some-url.com/relative_part?param1=value1&param2=value2'
