from functions.level_1_5.five_replace_word import replace_word
import pytest

@pytest.mark.parametrize(
        "text,replace_from,replace_to,expected_result",
        [
            ("Говорил попугай попугаю: Я тебя попугай попугаю. Отвечает ему \
             попугай : Попугай , попугай , попугай !", "Попугай", "воробей",
             "Говорил воробей попугаю: Я тебя воробей попугаю. Отвечает ему воробей : воробей , воробей , воробей !"),
            ("У елки иголки колки", "хвойное", "дерево", "У елки иголки колки")
        ],
        ids=[
            "change repeated word in replace from in all text",
            "inputed text will not changed when no words consisted with replace from"
        ]
)
def test__replace_word__successfull(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result
