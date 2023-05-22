from functions.level_1_5.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__GOOD_sentiment():

    good_words = {'изумительно', 'очаровательно', 'исключительно'}
    bad_words = {'идиотский', 'бездарный', 'бесталанный'}
    text = 'Общая оценка: изумительно! Исключительно профессиональная работа. \
        Очаровательно решительно все'

    sentiment = check_tweet_sentiment(text, good_words, bad_words)

    assert sentiment == "GOOD"


def test__check_tweet_sentiment__BAD_sentiment():

    good_words = {'изумительно', 'очаровательно', 'исключительно'}
    bad_words = {'идиотский', 'бездарный', 'бесталанный'}
    text = 'Кто вел этот идиотский концерт? БЕЗДАРНЫЙ текст и \
        бесталанный исполнитель'

    sentiment = check_tweet_sentiment(text, good_words, bad_words)

    assert sentiment == "BAD"


def test__check_tweet_sentiment__sarcastic_sentiment():

    good_words = {'изумительно', 'очаровательно', 'исключительно'}
    bad_words = {'идиотский', 'бездарный', 'бесталанный'}
    text = "Изумительно бездарный фильм. Очаровательно бесталанный актер \
        и исключительно идиотский сценарий"

    sentiment = check_tweet_sentiment(text, good_words, bad_words)

    assert sentiment is None
