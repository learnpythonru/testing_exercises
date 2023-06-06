from functions.level_1_5.five_replace_word import replace_word


def test__replace_word__change_repeated_word_in_replace_from_in_all_text():

    text = "Говорил попугай попугаю: Я тебя попугай попугаю. Отвечает ему \
        попугай : Попугай , попугай , попугай !"
    replace_from = "Попугай"
    replace_to = "воробей"

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == "Говорил воробей попугаю: Я тебя воробей попугаю. Отвечает ему воробей : воробей , воробей , воробей !"

def test__replace_word__inputed_text_will_not_changed_when_no_words_consisted_with_replace_from():

    text = "У елки иголки колки"
    replace_from = "хвойное"
    replace_to = "дерево"

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == "У елки иголки колки"
