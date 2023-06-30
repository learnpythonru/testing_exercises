import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
        "host_name,relative_url,params,expected_outp",
        [
            ('https://www.youtube.com', 'watch', {'v':'dQw4w9WgXcQ'}, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
            ('https://translate.google.com', 'saved', {'hl': 'ru', 'sl': 'en', 'tl': 'ru', 'op': 'images'}, 'https://translate.google.com/saved?hl=ru&sl=en&tl=ru&op=images'),
            ('https://github.com', 'MagerOK/testing_exercises', None, 'https://github.com/MagerOK/testing_exercises'),
        ],
        ids=[
            ('Build url with only 1 parameter'),
            ('Build url with more parameters'),
            ('Build url without any parameters'),
        ]
)
def test__build_url(host_name, relative_url, params, expected_outp):
    assert build_url(host_name, relative_url, params) == expected_outp