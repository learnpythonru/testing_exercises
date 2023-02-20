from typing import Mapping

import pytest

from functions.three_url_builder import build_url

hostname = "https://market.yandex.ru"
relative_url_value = "catalog"
get_params_value = {
    "product_id": "1",
    "color": "red",
}


@pytest.mark.parametrize(
    "expected, host_name, relative_url, get_params",
    [
        (
            f"{hostname}/{relative_url_value}",
            hostname,
            relative_url_value,
            None,
        ),
        (
            f"{hostname}/{relative_url_value}",
            hostname,
            relative_url_value,
            {},
        ),
        (
            f"{hostname}/{relative_url_value}?product_id=1&color=red",
            hostname,
            relative_url_value,
            get_params_value,
        ),
    ],
)
def test_build_url(
    expected: str,
    host_name: str,
    relative_url: str,
    get_params: Mapping[str, str],
):
    assert build_url(host_name, relative_url, get_params) == expected
