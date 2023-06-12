from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
        'text, good_words, bad_words, expected_result',
        [
            (
                'I love this movie',
                {'love', 'great', 'awesome'},
                {'hate', 'terrible', 'awful'},
                'GOOD',
            ),
            (
                'This pizza is disgusting',
                {'love', 'great', 'awesome'},
                {'disgusting', 'terrible', 'awful'},
                'BAD',
            ),
            (
                'The product has good features, but the customer support is bad',
                {'good', 'excellent', 'impressive'},
                {'bad', 'poor', 'disappointing'},
                None,
            ),
        ],
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected_result
