import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize('text, replace_from, replace_to, expected_result', [
    ('На улице шел сильный снег!', 'сильный', 'слабый', 'На улице шел слабый снег!'),
    ('Это был замечательный день!', 'замечательный', 'замечательный', 'Это был замечательный день!'),
    ('На улице шел мокрый снег!', 'сильный', 'слабый', 'На улице шел мокрый снег!'),
    ('На улице шел мокрый снег!', '', 'слабый', 'На улице шел мокрый снег!'),
    ('', 'name', 'surname', ''),
    ('123 456 789', '123', '321', '321 456 789'),
    ('По улице проехала БОЛЬШАЯ машина', 'большая', 'МАЛЕНЬКАЯ', 'По улице проехала МАЛЕНЬКАЯ машина')
])
def test__replace_word__succes(text, replace_from, replace_to, expected_result):
    assert replace_word(text=text, replace_from=replace_from,
                        replace_to=replace_to) == expected_result
