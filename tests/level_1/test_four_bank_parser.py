import datetime
import decimal

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    sms = SmsMessage(
        text="Вы купили 0.23 Эфира, *1234 18.05.23 23:59 MEWWALLET authcode 5005",
        author="MewWallet",
        sent_at=datetime.datetime.now(),
    )

    cards = [
        BankCard("1234", "Pavel Mager"),
        BankCard("5678", "Pavel Mager"),
    ]

    expected_output = Expense(
        amount=decimal.Decimal("0.23"),
        card=cards[0],
        spent_in="MEWWALLET",
        spent_at=datetime.datetime.strptime("18.05.23 23:59", "%d.%m.%y %H:%M"),
    )
    assert parse_ineco_expense(sms, cards) == expected_output