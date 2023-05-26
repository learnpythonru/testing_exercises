from functions.level_1_5.four_sentiment import check_tweet_sentiment

def test_check_tweet_sentiment_with_only_good_words():
    text = 'This text with only good words'
    good_words = ['good', 'best', 'perfect']
    bad_words = ['bad', 'scary', 'terrible']
    assert check_tweet_sentiment(text, good_words, bad_words) == 'GOOD'

def test_check_tweet_sentiment_with_only_bad_words():
    text = 'This text with only bad words'
    good_words = ['good', 'best', 'perfect']
    bad_words = ['bad', 'scary', 'terrible']
    assert check_tweet_sentiment(text, good_words, bad_words) == 'BAD'

def test_check_tweet_sentiment_with_equal_good_and_bad_words():
    text = 'This text with good and bad words'
    good_words = ['good', 'best', 'perfect']
    bad_words = ['bad', 'scary', 'terrible']
    assert check_tweet_sentiment(text, good_words, bad_words) == None

def test_check_tweet_sentiment_without_good_and_bad_words():
    text = 'This text without needed words'
    good_words = ['good', 'best', 'perfect']
    bad_words = ['bad', 'scary', 'terrible']
    assert check_tweet_sentiment(text, good_words, bad_words) == None