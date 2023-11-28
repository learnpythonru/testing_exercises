import pytest

from functions.level_2.five_replace_word import replace_word


# def replace_word(text: str, replace_from: str, replace_to: str) -> str:
#     words = text.split()

#     new_words = []
#     for word in words:
#         if word.lower() == replace_from.lower():
#             new_words.append(replace_to)
#         else:
#             new_words.append(word)

#     return ' '.join(new_words)


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


@pytest.mark.parametrize('text, replace_from, replace_to, expected_error', [
    (123, '123', '321', AttributeError),
    ('123 456 789', '123', 321, TypeError),
])
def test__replace_word__with_error(text, replace_from, replace_to, expected_error):
    with pytest.raises(expected_error):
        replace_word(text=text, replace_from=replace_from, replace_to=replace_to)
