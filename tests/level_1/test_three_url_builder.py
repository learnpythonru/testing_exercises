from functions.level_1.three_url_builder import build_url
import pytest


@pytest.mark.parametrize(
    'host_name,relative_url,expected',
    [
        ('russianfood', 'recipes', 'russianfood/recipes'),
        (
            ['russianfood', 'recipes'],
            {'name': 'borsch', 'vegan': '0'},
            "['russianfood', 'recipes']/{'name': 'borsch', 'vegan': '0'}",
        ),
        (100, 5, "100/5"),
     ]
)
def test_build_url_without_get_params(host_name, relative_url, expected):
    assert build_url(host_name, relative_url) == expected


@pytest.mark.parametrize(
    'host_name,relative_url,get_params',
    [
        ('russianfood', 'recipes', False),
        ('russianfood', 'recipes', 0)
    ])
def test_build_url_with_false_get_params(host_name, relative_url, get_params):
    assert build_url(host_name, relative_url, get_params) == 'russianfood/recipes'


@pytest.mark.parametrize(
    'host_name,relative_url,get_params',
    [
        ('russianfood', 'recipes', True),
        ('russianfood', 'recipes', ['borsch', 'vegan']),
        ('russianfood', 'recipes', 'borsch'),
    ]
)
def test_build_url_with_not_dict_get_params(host_name, relative_url, get_params):
    with pytest.raises(AttributeError):
        build_url(host_name, relative_url, get_params)


def test_build_url_without_non_default_args():
    with pytest.raises(TypeError):
        build_url()