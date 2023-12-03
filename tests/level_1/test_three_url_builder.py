from functions.level_1.three_url_builder import build_url


def test__build_url__with_params():
    assert build_url('https://www.youtube.com', 'watch', get_params={'v':'dQw4w9WgXcQ'}) == 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
def test__build_url__without_params():
    assert build_url('https://github.com', 'MagerOK/testing_exercises') == 'https://github.com/MagerOK/testing_exercises'

