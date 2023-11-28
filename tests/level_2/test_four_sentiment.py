import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment

# def check_tweet_sentiment(text: str, good_words: set[str], bad_words: set[str]) -> str | None:
#     words = [w.lower() for w in text.split()]
#     good_words_num = sum(1 for w in words if w in good_words)
#     bad_words_num = sum(1 for w in words if w in bad_words)
#     if not good_words_num and not bad_words_num or good_words_num == bad_words_num:
#         return None
#     if good_words_num > bad_words_num:
#         return 'GOOD'
#     return 'BAD'

good_words = {'позитив', 'восхитительно', 'удивительно', 'радостно',
              'великолепно', 'хорошо', 'прекрасно', 'интересно'}

bad_words = {'негатив', 'печально', 'разочарование', 'плохо',
             'грустно', 'нудно', 'проблемы', 'скучно', 'раздражение'}


@pytest.mark.parametrize('text, good_words, bad_words, expected_result', [
    ('Этот текст не несет в себе никаких эмоций.',
     good_words, bad_words, None),
    ('Погода сегодня так себе, не слишком хорошо, но и не плохо. Все как обычно.',
     good_words, bad_words, None),
    ('Сегодня просто восхитительно! На улице прекрасно, удивительно солнечно и интересно.',
     good_words, bad_words, 'GOOD'),
    ('У меня проблемы, кругом один негатив, это печально и грустно.',
     good_words, bad_words, 'BAD'),
    ('Some_long_long_long_long_text', good_words, bad_words, None),
])
def test__check_tweet_sentimemt__succes(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text=text, good_words=good_words,
                                 bad_words=bad_words) == expected_result


@pytest.mark.parametrize('text, good_words, bad_words, expected_error', [
    (123, {'good', 'word'}, {'bad', 'word'}, AttributeError),
    ('Some text', 123, {'bad', 'evil'}, TypeError),
])
def test__check_tweet_sentiment__with_error(text, good_words, bad_words, expected_error):
    with pytest.raises(expected_error):
        check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words)
