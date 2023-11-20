import datetime
import decimal

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


@pytest.fixture
def base_sms():
    return SmsMessage(
        text='123.45 RUB, 5559123456789012 20.11.23 21:00 SOFA_SHOP authcode 123456',
        author='My Bank',
        sent_at=datetime.datetime.now()
    )


@pytest.fixture
def base_cards():
    return [BankCard(
        last_digits='9012',
        owner='Eugene'
    ),
        BankCard(
            last_digits='1234',
            owner='Daria'
        )
    ]


def test_parse_ineco_expense(base_sms, base_cards):
    assert parse_ineco_expense(base_sms, base_cards) == Expense(
        amount=decimal.Decimal('123.45'),
        card=BankCard(last_digits='9012', owner='Eugene'),
        spent_in='SOFA_SHOP',
        spent_at=datetime.datetime.strptime(f'20.11.23 21:00', '%d.%m.%y %H:%M')
    )

