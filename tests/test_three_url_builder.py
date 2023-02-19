from typing import Mapping

import pytest

from functions.three_url_builder import build_url


@pytest.mark.parametrize(
    "expected, host_name, relative_url, get_params",
    [
        (
            pytest.lazy_fixture("url_without_params"),
            pytest.lazy_fixture("hostname_value"),
            pytest.lazy_fixture("relative_url_value"),
            None,
        ),
        (
            pytest.lazy_fixture("url_without_params"),
            pytest.lazy_fixture("hostname_value"),
            pytest.lazy_fixture("relative_url_value"),
            [],
        ),
        (
            pytest.lazy_fixture("url_with_params"),
            pytest.lazy_fixture("hostname_value"),
            pytest.lazy_fixture("relative_url_value"),
            pytest.lazy_fixture("get_params_value"),
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
