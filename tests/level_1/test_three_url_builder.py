from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('https://www.youtube.com', 'watch', get_params={'v':'dQw4w9WgXcQ'}) == 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    assert build_url('https://github.com', 'MagerOK/testing_exercises') == 'https://github.com/MagerOK/testing_exercises'

