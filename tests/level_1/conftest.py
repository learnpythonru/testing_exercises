import datetime

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage


@pytest.fixture
def bank_card_list() -> list[BankCard]:
    return [
        BankCard(last_digits="1234", owner="John Doe"),
        BankCard(last_digits="5678", owner="Jane Smith"),
    ]


@pytest.fixture
def sms_list() -> list[SmsMessage]:
    return [
        SmsMessage(text='2500.00 RUB, 112223331234 18.11.23 13:31 Magnit authcode 5522',
                   author='Bank', sent_at=datetime.datetime.now()),
        SmsMessage(text='1200.50 RUB, 445566775678 19.01.24 15:45 Walmart authcode 1234',
                   author='Bank', sent_at=datetime.datetime.now()),
        SmsMessage(text='150.50 RUB, 445566775676 15.01.24 12:45 Ozon authcode 1254',
                   author='Bank', sent_at=datetime.datetime.now()),
        SmsMessage(text='0 RUB, 445566775678 19.01.24 15:45 Wildberries authcode 1234',
                   author='Bank', sent_at=datetime.datetime.now()),
    ]
