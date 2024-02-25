from functions.level_1_5.five_replace_word import replace_word


def test__replace_word__with_replaces():
    text = 'I have the power that my father never dreamed of! NEVER !!!'
    replace_from = 'never'
    replace_to = 'always'
    exp_output = 'I have the power that my father always dreamed of! always !!!'
    assert replace_word(text, replace_from, replace_to) == exp_output

def test__replace_word__without_replaces():
    text = 'I have the power that my father never dreamed of! NEVER !!!'
    replace_from = 'Sponge'
    replace_to = 'Bob'
    assert replace_word(text, replace_from, replace_to) == text