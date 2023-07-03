from functions.level_2.four_lines_counter import count_lines_in
from unittest.mock import patch, mock_open


def test__count_lines_in__return_number_of_lines_without_hash():
    text = "1st line.\n #2st line.\n 3st line."
    with patch('functions.level_2.four_lines_counter.os.path.isfile') as os_path_is_file_mock:
        os_path_is_file_mock.return_value = True
        with patch('functions.level_2.four_lines_counter.open', mock_open(read_data=text)) as m:
            assert count_lines_in(m) == 2

def test__count_lines_in__return_none_when_no_file():
    assert count_lines_in("file.txt") is None


# вариант с фикстурой с yeld, проверить что фикстура удаляет файл
def test__count_lines_in__success(create_test_file):
    assert count_lines_in(create_test_file) == 2
