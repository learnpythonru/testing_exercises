from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest


def test__check_tweet_sentiment__return_positive_sentiment_when_good_words_are_more_then_bad_ones():

    good_words = {'изумительно', 'очаровательно', 'исключительно'}
    bad_words = {'идиотский', 'бездарный', 'бесталанный'}
    text = 'Общая оценка: изумительно! Исключительно профессиональная работа. \
        Очаровательно решительно все'

    sentiment = check_tweet_sentiment(text, good_words, bad_words)

    assert sentiment == "GOOD"


def test__check_tweet_sentiment__return_negative_sentiment_when_bad_words_are_more_then_good_ones():

    good_words = {'изумительно', 'очаровательно', 'исключительно'}
    bad_words = {'идиотский', 'бездарный', 'бесталанный'}
    text = 'Кто вел этот идиотский концерт? БЕЗДАРНЫЙ текст и \
        бесталанный исполнитель'

    sentiment = check_tweet_sentiment(text, good_words, bad_words)

    assert sentiment == "BAD"


def test__check_tweet_sentiment__when_number_of_good_and_bad_words_is_equal_in_text():

    good_words = {'изумительно', 'очаровательно', 'исключительно'}
    bad_words = {'идиотский', 'бездарный', 'бесталанный'}
    text = "Изумительно бездарный фильм. Очаровательно бесталанный актер \
        и исключительно идиотский сценарий"

    sentiment = check_tweet_sentiment(text, good_words, bad_words)

    assert sentiment is None


def test__check_tweet_sentiment__return_None_when_no_good_and_bad_words_in_assesment():

    good_words = {'изумительно', 'очаровательно', 'исключительно'}
    bad_words = {'идиотский', 'бездарный', 'бесталанный'}
    text = 'Ну такое..'

    sentiment = check_tweet_sentiment(text, good_words, bad_words)

    assert sentiment is None
