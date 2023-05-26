from functions.level_1_5.five_replace_word import replace_word

def test__replace_word__starts_with_case_irrelevant():
    assert replace_word('the big black car', 'big', 'Black') == 'the Black black car'


def test__replace_word__if_replace_word_not_find_in_text():
    assert replace_word('the big black car', 'red', 'small') == 'the big black car'

