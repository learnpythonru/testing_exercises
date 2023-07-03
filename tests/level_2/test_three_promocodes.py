from functions.level_2.three_promocodes import generate_promocode
from unittest.mock import patch
import string

def test__generate_promocode__return_default_number_of_letters():
    with patch('functions.level_2.three_promocodes.random.choice') as random_choice_mock:
        random_choice_mock.return_value = "A"
        assert generate_promocode() == "AAAAAAAA"

def test__generate_promocode__return_set_number_of_letters(random_choice_mock):
    random_choice_mock.return_value = "B"
    assert generate_promocode(promocode_len=3) == "BBB"

def test__generate_promocode__return_random_choice_called_once_with_params(random_choice_mock):
    random_choice_mock.return_value = "C"
    generate_promocode(promocode_len=1)
    random_choice_mock.assert_called_once_with(string.ascii_uppercase)
