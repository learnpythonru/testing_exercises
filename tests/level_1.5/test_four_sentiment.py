from functions.level_1_5.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__good():
    text = 'I love this movie'
    good_words = {'love', 'great', 'awesome'}
    bad_words = {'hate', 'terrible', 'awful'}
    exp_result = 'GOOD'

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == exp_result


def test__check_tweet_sentiment__bad():
    text = 'This pizza is disgusting'
    good_words = {'love', 'great', 'awesome'}
    bad_words = {'disgusting', 'terrible', 'awful'}
    exp_result = 'BAD'

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == exp_result


def test__check_tweet_sentiment__none():
    text = 'The product has good features, but the customer support is bad'
    good_words = {'good', 'excellent', 'impressive'}
    bad_words = {'bad', 'poor', 'disappointing'}
    exp_result = None

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == exp_result