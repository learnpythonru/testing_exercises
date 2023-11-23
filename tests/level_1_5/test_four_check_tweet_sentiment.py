from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest



def test__check_tweet_sentiment__one_length_for_gw_and_bw():
    assert check_tweet_sentiment('g1 b1 g2 b2 g3 b3 ', {'g1','g2'}, {'b1', 'b2'}) == 'BAD'


def test__check_tweet_sentiment__not_bw_and_gw_in_text():
    assert check_tweet_sentiment('g0 b0 g0 b0 g3 b3 ', {'g1','g2'}, {'b1', 'b2'}) == None


def test__check_tweet_sentiment_gw_equal_to_bw():     
    assert check_tweet_sentiment('g1 b2 g0 b0 g3 b3 ', {'g1','g2'}, {'g1', 'g2'}) == None


def test__check_tweet_sentiment__gw_longer_than_bw():
    assert check_tweet_sentiment('g1 b2 g0 b0 g3 b3 g4 b4', {'g1','g2', 'g3'}, {'g1', 'g2'}) == 'GOOD'


def test__check_tweet_sentiment__no_set_in_gw_and_bw():
    assert check_tweet_sentiment('1 2', '5 6 7 4', '2') == 'GOOD'


def test__check_tweet_sentiment__gw_longer_than_bw_and_nothing_in_text():    
    assert check_tweet_sentiment('g0 b0 g0 b0 g0 b3 g4 b4', {'g1','g2', 'g3'}, {'g1', 'g2'}) == None


def test__check_tweet_sentiment__gw_shorter_than_bw_and_bw_in_text():     
    assert check_tweet_sentiment('g0 b0 g3 b3 g4 b4', {'g1','g2'}, {'g1', 'g2', 'g3'}) == 'BAD'


def test__check_tweet_sentiment__gw_shorter_than_bw_and_bw_in_text():
    assert check_tweet_sentiment('g0 b0 g3  b3 g4 b4', {''}, {'g1', 'g2', 'g3'}) == 'BAD'


def test__check_tweet_sentiment__gw_and_bw_empty():
    assert check_tweet_sentiment('g0 b0 g3  b3 g4 b4', {''}, {''}) == None


def test__check_tweet_sentiment__everything_is_empty():
    assert check_tweet_sentiment('', {''}, {''}) == None


def test__check_tweet_sentiment__everything_is_str():    
    assert check_tweet_sentiment('one two', 'one', 'two') == 'BAD'


def test__check_tweet_sentiment__no_bw_typeerror():
    with pytest.raises(TypeError):
        check_tweet_sentiment('', {''})


def test__check_tweet_sentiment__text_is_int_attributeerror():
    with pytest.raises(AttributeError):
        check_tweet_sentiment(123, '5 6 7 4', '2')