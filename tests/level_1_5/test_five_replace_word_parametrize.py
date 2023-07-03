from functions.level_1_5.five_replace_word import replace_word
import pytest

@pytest.mark.parametrize(
        "text,replace_from,replace_to,expected_result",
        [
            ("Сначала бежим , потом бежим", "бежим", "лежим", "Сначала лежим , потом лежим"),
            ("сидим едим", "сидим", "спим", "спим едим")
        ]
)
def test__replace_word__successfull_change_repeated_word_in_replace_from_in_all_text(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(
        "text,replace_from,replace_to,expected_result",
        [
            ("Шли шли , не дошли", "ехали", "приехали", "Шли шли , не дошли"),
            ("Любовь, смерть и роботы", "кино", "мульт", "Любовь, смерть и роботы")
        ]
)
def test__replace_word__fail(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result
