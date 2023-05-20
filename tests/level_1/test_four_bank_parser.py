from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import pytest
import decimal

def test_parse_ineco_expense():
    sms = SmsMessage(
        text="100.00 RUB. CARD1234, authcode 1234. 01.01.23 11:30",
        author="Alfa Bank",
        sent_at=datetime.datetime(2023, 1, 1, 11, 30)
    )
    cards = [
        BankCard(last_digits="1234", owner= "Alex"),
        BankCard(last_digits="5678", owner= "Alexandr"),
    ]
    result = parse_ineco_expense(sms, cards)
    expected = Expense(
        amount=decimal.Decimal("100.00"),
        card=BankCard(last_digits="1234"),
        spent_in="CARD1234",
        spent_at=datetime.datetime(2023, 1, 1, 11, 30),
    )
    assert result == expected

    with pytest.raises(ValueError):
        parse_ineco_expense(sms, cards)