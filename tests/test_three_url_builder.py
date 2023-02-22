from functions.three_url_builder import build_url
import pytest


@pytest.mark.parametrize(
    'host_name, relative_url, get_params, expected_result',
    [
        ('hh.ru', 'applicant/negotiations', {
            'hhtmFrom': 'employer', 'hhtmFromLabel': 'header'
        }, 'hh.ru/applicant/negotiations?hhtmFrom=employer&hhtmFromLabel=header'),
        ('hh.ru', 'applicant/negotiations', {}, 'hh.ru/applicant/negotiations'),
        ('hh.ru', 'applicant/negotiations', None, 'hh.ru/applicant/negotiations')
    ]
    )
def test_build_url(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result
