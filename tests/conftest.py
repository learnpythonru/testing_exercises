import pytest
from datetime import datetime
from functions.four_bank_parser import SmsMessage, Expense, BankCard
from decimal import Decimal


@pytest.fixture
def max_string():
    return ''.join('s' for n in range(100))


@pytest.fixture
def sms_text():
    return '1020 руб, 4400430255123326 20.02.23 16:20 7/11 authcode 3034'


@pytest.fixture
def sms_message(sms_text):
    return SmsMessage(
        text=sms_text,
        author="Sberbank",
        sent_at=datetime(2023, 2, 20, 16, 20, 20),
    )


@pytest.fixture
def bank_card():
    return [
        BankCard(last_digits='3326', owner='Nikita T.'),
        BankCard(last_digits='1815', owner='Olga N.'),
        BankCard(last_digits='1855', owner='Roman G.'),
    ]


@pytest.fixture
def expense():
    return Expense(
        amount=Decimal('1020'),
        card=BankCard(last_digits='3326', owner='Nikita T.'),
        spent_in='7/11',
        spent_at=datetime(2023, 2, 20, 16, 20),
    )