import datetime
import decimal
from typing import NamedTuple
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    test_cards = [BankCard(last_digits='12345', owner='matching_card_owner_1'),
                  BankCard(last_digits='54321', owner='non_matching_card_owner_1'),
                  BankCard(last_digits='12345', owner='matching_card_owner_2')]

    test_sms_msg = SmsMessage(text='', author="test_author")
    raise NotImplementedError("TODO: implement after receiving infod")

