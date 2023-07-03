from functions.level_2.one_brackets import delete_remove_brackets_quotes
import pytest
from unittest.mock import patch


@pytest.mark.xfail
def test__delete_remove_brackets_quotes__string_with_brackets_return_incomplete_string():
    with patch('functions.level_2.one_brackets.len') as len_mock:
        len_mock.return_value = 7
        assert delete_remove_brackets_quotes('{home}') == 'ome'



def test__delete_remove_brackets_quotes__success_string_without_brackets():
    assert delete_remove_brackets_quotes('abcd') == 'abcd'
