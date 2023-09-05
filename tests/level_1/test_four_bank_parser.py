import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
from decimal import Decimal

sms_ok = SmsMessage(
    text='Покупка 56 р., "MIR-8664 04.04.23 18:14 Mos.Transport 41 MIRA authcode 245896',
    author='900',
    sent_at=datetime.datetime.strptime('04/14/23 18:15:26', '%m/%d/%y %H:%M:%S')
)

sms_with_wrong_card_num = SmsMessage(
    text='Покупка 56 р., "MIR-8665 04.04.23 18:14 Mos.Transport 41 MIRA authcode 245896',
    author='900',
    sent_at=datetime.datetime.strptime('04/14/23 18:15:26', '%m/%d/%y %H:%M:%S')
)

sms_without_comma = SmsMessage(
    text='Покупка 56 р. "MIR-8664 04.04.23 18:14 Mos.Transport 41 MIRA authcode 245896',
    author='900',
    sent_at=datetime.datetime.strptime('04/14/23 18:15:26', '%m/%d/%y %H:%M:%S')
)


@pytest.fixture
def expense():
    return Expense(
        amount=Decimal('56'),
        card=BankCard(
            last_digits='8664',
            owner='IVAN IVANOV'
        ),
        spent_in='Mos.Transport 41 MIRA',
        spent_at=datetime.datetime(2023, 4, 4, 18, 14)
    )


@pytest.fixture
def cards():
    return [
        BankCard(
            last_digits='8664',
            owner='IVAN IVANOV'
        ),
        BankCard(
            last_digits='8564',
            owner='IVAN GROZNYJ'
        ),
        BankCard(
            last_digits='4789',
            owner='MALYUTA SCURATOV'
        )
    ]


def test_parse_ineco_expense(cards, expense):
    assert parse_ineco_expense(sms=sms_ok, cards=cards) == expense


def test_parse_ineco_expense_with_wrong_card_in_sms(cards):
    with pytest.raises(IndexError):
        parse_ineco_expense(sms=sms_with_wrong_card_num, cards=cards)


def test_parse_ineco_expense_without_comma_in_sms(cards):
    with pytest.raises(ValueError):
        parse_ineco_expense(sms=sms_without_comma, cards=cards)
