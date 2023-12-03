from functions.level_1_5.five_replace_word import replace_word
import pytest

def replace_word(text: str, replace_from: str, replace_to: str) -> str:
    words = text.split()

    new_words = []
    for word in words:
        if word.lower() == replace_from.lower():
            new_words.append(replace_to)
        else:
            new_words.append(word)

    return ' '.join(new_words)



@pytest.mark.parametrize(
  "text, replace_from, replace_to, expected_result",
  [
    ('one two three four', 'two', 'replace_to', 'one replace_to three four'),
    ('one two three Two four', 'two', 'replace_to','one replace_to three replace_to four'),
    ('one two three four', 'TWo', 'replace_to','one replace_to three four'),
    ('one two three four', '1234', 'replace_to', 'one two three four'), 
    ('one two three four', '', 'replace_to', 'one two three four'),
    ('one two three four', 'two', '', 'one  three four'),
  ]
)

def test__replace_word__is_valif(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result


def test__replace_word__replace_to_is_int_typeerror():
        with pytest.raises(TypeError):
            replace_word('one two three four', 'two', 123)


def test__replace_word__replace_from_is_int_attributeerror():
    with pytest.raises(AttributeError):
        replace_word('one two three four', 2, '123')


def test__replace_word__text_is_int_attributeerror():
    with pytest.raises(AttributeError):
        replace_word(123314, 'two', '123')


def test__replace_word__not_enough_params_typeerror():
    with pytest.raises(TypeError):   
        replace_word('123', 'bsrbg')