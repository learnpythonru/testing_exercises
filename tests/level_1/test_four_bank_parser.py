from functions.level_1.four_bank_parser import parse_ineco_expense
import pytest


def test__parse_ineco_expense__success(bank_card_1234, bank_card_5678, sms_message, expense):
    cards = [bank_card_1234, bank_card_5678]

    result = parse_ineco_expense(sms_message, cards)

    assert result == expense


def test__parse_ineco_expense__invalid_format(bank_card_5678, sms_message):
    cards = [bank_card_5678]

    with pytest.raises(IndexError):
        parse_ineco_expense(sms_message, cards)
