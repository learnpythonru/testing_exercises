import pytest

from functions.level_1.one_gender import genderalize


@pytest.fixture
def base_gender_data():
    return 'He goes', 'She goes'


def test_genderalize_male(base_gender_data):
    assert genderalize(base_gender_data[0], base_gender_data[1], 'male') == base_gender_data[0]


def test_genderalize_female(base_gender_data):
    assert genderalize(base_gender_data[0], base_gender_data[1], 'female') == base_gender_data[1]


def test_return_type():
    assert type(genderalize('goes', 'goes', 'male') == type(str))
