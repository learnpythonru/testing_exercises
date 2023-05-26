from functions.level_1_5.five_replace_word import replace_word

def test_replace_word_starts_with_low_letter():
    assert replace_word('the big black car', 'big', 'black') == 'the black black car'

def test_replace_word_starts_with_capital_letter():
    assert replace_word('the big black car', 'Big', 'Black') == 'the Black black car'

def test_replace_word_if_replace_word_not_find_in_text():
    assert replace_word('the big black car', 'black', 'small') == 'the big small car'

