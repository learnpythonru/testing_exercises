from functions.level_1_5.five_replace_word import replace_word


def replace_word(text: str, replace_from: str, replace_to: str) -> str:
    words = text.split()

    new_words = []
    for word in words:
        if word.lower() == replace_from.lower():
            new_words.append(replace_to)
        else:
            new_words.append(word)

    return ' '.join(new_words)


def test__replace_word__change_one_word():

    text = "Говорил попугай попугаю: Я тебя попугай попугаю. Отвечает ему \
        попугай : Попугай , попугай , попугай !"
    replace_from = "Попугай"
    replace_to = "воробей"

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == "Говорил воробей попугаю: Я тебя воробей попугаю. Отвечает ему воробей : воробей , воробей , воробей !"

def test__replace_word__no_changes():

    text = "У елки иголки колки"
    replace_from = "хвойное"
    replace_to = "дерево"

    new_text = replace_word(text, replace_from, replace_to)

    assert new_text == "У елки иголки колки"
