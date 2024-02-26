from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
"text, good_words, bad_words, expected_result",
[
   ('g1 b1 g2 b2 g3 b3 ', {'g1','g2'}, {'b1', 'b2'}, None), 
   ('g0 b0 g0 b0 g3 b3 ', {'g1','g2'}, {'b1', 'b2'}, None),
   ('g1 b2 g0 b0 g3 b3 ', {'g1','g2'}, {'g1', 'g2'}, None),
   ('g1 b2 g0 b0 g3 b3 g4 b4', {'g1','g2', 'g3'}, {'g1', 'g2'},'GOOD'),
   ('1 2', '5 6 7 4', '2', 'BAD'),
   ('g0 b0 g0 b0 g0 b3 g4 b4', {'g1','g2', 'g3'}, {'g1', 'g2'}, None),
   ('g0 b0 g3 b3 g4 b4', {'g1','g2'}, {'g1', 'g2', 'g3'},'BAD'),
   ('g0 b0 g3  b3 g4 b4', {''}, {'g1', 'g2', 'g3'}, 'BAD'),
   ('g0 b0 g3  b3 g4 b4', {''}, {''}, None),
   ('', {''}, {''}, None),
    ('one two', 'one', 'two', None),
]
)

def test__check_tweet_sentiment__is_valid(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) is expected_result


@pytest.mark.parametrize(
"text, good_words, bad_words, expected_error",
[
 #   ('', {''}, TypeError),
    (123, '5 6 7 4', '2', AttributeError),
]
)

def test__check_tweet_sentiment__errors(text, good_words, bad_words, expected_error):
    with pytest.raises(expected_error):
        check_tweet_sentiment(text, good_words, bad_words)

