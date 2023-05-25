from functions.level_1_5.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__without_any_bad_or_good_words():
    text = "This is an ordinary text, without any emotional expressions."
    good_words = set()
    bad_words = set()
    assert check_tweet_sentiment(text, good_words, bad_words) == None

def test__check_tweet_sentiment__with_the_same_number_of_words():
    text = "Very good, so good, it'so good, Jesus! But I hate it! It's disgusting! I hate it! I FUCKING HATE IT YOU HEAR ME?"
    good_words = {'good,', 'jesus!'}
    bad_words = {'hate', 'fucking'}
    assert check_tweet_sentiment(text, good_words, bad_words) == None

def test__check_tweet_sentiment__normal_expecting_BAD_response():
    text = "You motherfucker, come on, you little ass… fuck with me, eh?! You fucking little asshole, dickhead, cocksucker… You fuckin’ — come on, come fuck with me! I’ll get your ass, you jerk! Oh, you fuckhead, motherfucker! Fuck all you and your family! Come on, you cocksucker, slime bucket, shitface, turdball! Come on, you scum sucker, you fucking with me?! Come on, you asshole!"
    good_words = {'family!', 'handsome', 'smart'}
    bad_words = {'fuck', 'fucking', 'ass...'}
    assert check_tweet_sentiment(text, good_words, bad_words) == 'BAD'

def test__check_tweet_sentiment__normal_expecting_GOOD_response():
    text = "I love this place! it's perfect to suicide for sure. i love it!"
    good_words = {'love'}
    bad_words = {'suicide'}
    assert check_tweet_sentiment(text, good_words, bad_words) == 'GOOD'