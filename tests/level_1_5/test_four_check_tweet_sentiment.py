from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
"text, good_words, bad_words, expected_result",
[
   ('g1 b1 g2 b2 g3 b3 ', {'g1','g2'}, {'b1', 'b2'}, 'BAD'), 
   ('g0 b0 g0 b0 g3 b3 ', {'g1','g2'}, {'b1', 'b2'}, None),
   ('g1 b2 g0 b0 g3 b3 ', {'g1','g2'}, {'g1', 'g2'}, None),
   ('g1 b2 g0 b0 g3 b3 g4 b4', {'g1','g2', 'g3'}, {'g1', 'g2'},'GOOD'),
   ('1 2', '5 6 7 4', '2', 'GOOD'),
   ('g0 b0 g0 b0 g0 b3 g4 b4', {'g1','g2', 'g3'}, {'g1', 'g2'}, None),
   ('g0 b0 g3 b3 g4 b4', {'g1','g2'}, {'g1', 'g2', 'g3'},'BAD'),
   ('g0 b0 g3  b3 g4 b4', {''}, {'g1', 'g2', 'g3'}, 'BAD'),
   ('g0 b0 g3  b3 g4 b4', {''}, {''}, None),
   ('', {''}, {''}, None),
   ('one two', 'one', 'two', 'BAD'),
]
)

def test__check_tweet_sentiment__is_valid(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) is expected_result


def test__check_tweet_sentiment__everything_is_str():    
    assert check_tweet_sentiment('one two', 'one', 'two') == 'BAD'


def test__check_tweet_sentiment__no_bw_typeerror():
    with pytest.raises(TypeError):
        check_tweet_sentiment('', {''})


def test__check_tweet_sentiment__text_is_int_attributeerror():
    with pytest.raises(AttributeError):
        check_tweet_sentiment(123, '5 6 7 4', '2')