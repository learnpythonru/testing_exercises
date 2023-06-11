from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
        "text,good_words,bad_words,expected_result",
        [
            ('Общая оценка: изумительно', {'изумительно'}, {'идиотский'}, "GOOD"),
            ('Кто вел этот идиотский концерт?', {'очаровательно'}, {'идиотский'}, "BAD"),
            ("Исключительно бездарный фильм", {'исключительно'}, {'бездарный'}, None),
            ('Ну такое..', {'исключительно'}, {'бесталанный'}, None),
        ],
        ids=[
            "return positive sentiment when good words more then bad",
            "return negative sentiment when bad words more then good",
            "when number of good and bad words is equal in text",
            "return None when no good and bad words in assesment"
        ]
)
def test__check_tweet_sentiment__successfull(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result

