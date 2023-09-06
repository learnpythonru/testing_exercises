from collections import namedtuple
from decimal import Decimal
import datetime


from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    # Test card data
    bank_card_tuple = namedtuple('BankCard', 'last_digits owner')
    bc1 = bank_card_tuple(last_digits='6969', owner='Dyadya Vanya')
    card = BankCard(*bc1)

    # Test sms data
    sms_tuple = namedtuple('SmsMessage', 'text author sent_at')
    sms1 = sms_tuple(text='42 amount, 6969 22.11.23 22:22 999999 authcode yes', author='Scrooge', sent_at='2023, 9, 6, 1, 28, 52, 999999')
    sms_message = SmsMessage(*sms1)

    test_data = Expense(amount=Decimal('42'), card=BankCard(last_digits='6969', owner='Dyadya Vanya'), spent_in='999999', spent_at=datetime.datetime(2023, 11, 22, 22, 22))
    assert parse_ineco_expense(sms_message, [card]) == test_data