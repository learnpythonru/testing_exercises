import pytest

from functions.level_1.five_title import change_copy_item

@pytest.mark.parametrize(
        'title,max_title_length,expected_outp',
        [
            ('Banana', 100, 'Copy of Banana'),
            ('Copy of Banana', 100, 'Copy of Banana (2)'),
            ('Copy of Banana (7)', 100, 'Copy of Banana (8)'),
            ('Banana', 3, 'Banana')
        ],
        ids=[
            "Adding 'Copy of' to title",
            'Make a copy of a first copy',
            'Increasing number of copy',
            'Limit lenght of a title',
        ]
)
def test__change_copy_item(title, max_title_length, expected_outp):
    assert change_copy_item(title, max_title_length) == expected_outp