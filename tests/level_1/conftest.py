import pytest
from datetime import datetime
from decimal import Decimal
from functions.level_1.four_bank_parser import BankCard, Expense, SmsMessage


@pytest.fixture
def bank_card_1234():
    return BankCard('1234', 'KONSTANTIN MISHAKOV')


@pytest.fixture
def bank_card_5678():
    return BankCard('5678', 'KONSTANTIN MISHAKOV')


@pytest.fixture
def expense_amount():
    return Decimal("99.99")


@pytest.fixture
def spent_in():
    return "nenaprasno.ru"


@pytest.fixture
def sms_message():
    return SmsMessage(
        f'{expense_amount} руб, *1234 12.04.23 16:00 nenaprasno.ru authcode 0000', "Tinkoff", datetime.now()
    )


@pytest.fixture
def expense():
    return Expense(
        amount=expense_amount,
        card=bank_card_1234,
        spent_in=spent_in,
        spent_at=datetime.strptime("12.04.23 16:00", "%d.%m.%y %H:%M"),
        )
