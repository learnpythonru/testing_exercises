import datetime
import decimal
from typing import NamedTuple


class BankCard(NamedTuple):
    last_digits: str
    owner: str


class SmsMessage(NamedTuple):
    text: str
    author: str
    sent_at: datetime.datetime


class Expense(NamedTuple):
    amount: decimal.Decimal
    card: BankCard
    spent_in: str
    spent_at: datetime.datetime


def parse_ineco_expense(sms: SmsMessage, cards: list[BankCard]) -> Expense:
    raw_sum, raw_details = sms.text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    raw_card, raw_date, raw_time, spend_in = raw_details.split(' ', maxsplit=3)
    return Expense(
        amount=decimal.Decimal(raw_sum.split(' ')[-2]),
        card=[c for c in cards if c.last_digits == raw_card[-4:]][0],
        spent_in=spend_in,
        spent_at=datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M'),
    )

from collections import namedtuple

bank_card_tuple = namedtuple('BankCard', 'last_digits owner')
bc1 = bank_card_tuple(last_digits=3344, owner='Dyadya Vanya')

card = BankCard(*bc1)
print(card)

# sms = SmsMessage(NamedTuple):
#     text: str
#     author: str
#     sent_at: datetime.datetime

# parse_ineco_expense(sms, cards)


