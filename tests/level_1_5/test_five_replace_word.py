from functions.level_1_5.five_replace_word import replace_word
import pytest

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
def test__replace_word__is_valid(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(
  "text, replace_from, replace_to, expected_error",
  [
    ('one two three four', 'two', 123, TypeError),
    ('one two three four', 2, '123', AttributeError),
    (123314, 'two', '123', AttributeError),
  ]
)
def test__replace_word__errors(text, replace_from, replace_to, expected_error):
        with pytest.raises(expected_error):
            replace_word(text, replace_from, replace_to)


def test__replace_word__not_enough_params_typeerror():
    with pytest.raises(TypeError):   
        replace_word('123', 'bsrbg')