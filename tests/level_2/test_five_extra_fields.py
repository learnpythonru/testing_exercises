import pytest

from functions.level_2.five_extra_fields import fetch_extra_fields_configuration, fetch_app_config_field


@pytest.mark.parametrize(
    "config_file_path, field_name, expected",
    [
        ("tests/files/config.ini", "extra_fields", "\ntest: str"),
        ("tests/files/config.ini", "no_fields", None),
        ("tests/files/no_config.ini", "no_fields", None),
    ],
)
def test__fetch_app_config_field(config_file_path: str, field_name: str, expected):
    assert fetch_app_config_field(config_file_path, field_name) == expected


@pytest.mark.parametrize(
    "config_file_path, expected",
    [
        ("tests/files/config.ini", {"test": str}),
        ("tests/files/no_config.ini", {}),
    ],
)
def test__fetch_extra_fields_configuration(config_file_path: str, expected):
    assert fetch_extra_fields_configuration(config_file_path) == expected
