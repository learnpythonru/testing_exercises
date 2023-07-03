from functions.level_2.five_extra_fields import fetch_app_config_field, fetch_extra_fields_configuration
from unittest.mock import patch


def test__fetch_app_config_field__success_created_file_with_three_lines_return_values(make_config):
    config_file_path = make_config(
        section="tool:app-config",
        field_name="extra_fields",
        field_value="line_1: 1 \n line_2: 2 \n line_3: 3"
        )
    field_name = "extra_fields"
    expected_value_1 = "line_1: 1"
    expected_value_2 = "line_2: 2"
    expected_value_3 = "line_3: 3"
    expected_value = expected_value_1 + "\n" + expected_value_2 + "\n" + expected_value_3
    assert fetch_app_config_field(config_file_path, field_name) == expected_value


def test__fetch_app_config_field__success_with_mock_used():
    with patch('functions.level_2.five_extra_fields.configparser.ConfigParser.__getitem__') as configparser_getitem_mock:
        configparser_getitem_mock.return_value = {"some_field": "some_values"}
        assert fetch_app_config_field("path_to_file", field_name="some_field") == "some_values"


def test__fetch_app_config_field__fail_with_mock_used_different_field_name():
    with patch('functions.level_2.five_extra_fields.configparser.ConfigParser.__getitem__') as configparser_getitem_mock:
        configparser_getitem_mock.return_value = {"some_field": "some_values"}
        assert fetch_app_config_field("path_to_file", field_name="other_field") is None


def test__fetch_app_config_field__return_none_when_section_is_not_app_config(make_config):
    config_file_path = make_config(
        section="some_section",
        field_name="example"
    )
    field_name = 'example'
    assert fetch_app_config_field(config_file_path, field_name) is None


def test__fetch_app_confiq_field__return_none_when_set_field_name_not_in_file(make_config):
    config_file_path = make_config(field_name="field")
    field_name = "extra_fields"
    assert fetch_app_config_field(config_file_path, field_name) is None


def test__fetch_extra_fields_configuration__success(make_config):
    config_file_path = make_config(
        section="tool:app-config",
        field_name="extra_fields",
        field_value="line_1: 1 \n line_2: 2 \n line_3: 3"
        )

    expected_value = {
        'line_1': 1,
        'line_2': 2,
        'line_3': 3
        }
    assert fetch_extra_fields_configuration(config_file_path) == expected_value


def test__fetch_extra_fields_configuration__return_empty_dict_when_no_extra_fields(make_config):
    config_file_path = make_config(field_name="field")
    assert fetch_extra_fields_configuration(config_file_path) == {}


def test__fetch_extra_fields_configuration_success_mock_used(config_mock):
    config_mock.return_value = {"extra_fields": "param_1: 10 \nparam_2: 20 \nparam_3: 30"}
    expected_value = {
        "param_1": 10,
        "param_2": 20,
        "param_3": 30
    }
    assert fetch_extra_fields_configuration('file_path') == expected_value


def test__fetch_extra_fields_configuration_success_mock_used_for_function():
    with patch('functions.level_2.five_extra_fields.fetch_app_config_field') as fetch_app_config_field_mock:
        fetch_app_config_field_mock.return_value = "val_1: 10 \nval_2: 20 \nval_3: 30"
        expected = {
            "val_1": 10,
            "val_2": 20,
            "val_3": 30
        }
        assert fetch_extra_fields_configuration('file_path') == expected