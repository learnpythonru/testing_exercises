import datetime
import decimal
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    cards = [BankCard(last_digits='1234', owner='John Doe'),
             BankCard(last_digits='5678', owner='Jane Doe')]
    sms = SmsMessage(
        text="100500 RUB, **1234 25.12.21 14:30 XYZ Store authcode 123456",
        author="Bank",
        sent_at=datetime.datetime.now()
    )

    result = parse_ineco_expense(sms, cards)

    assert isinstance(result, Expense)
    assert result.amount == decimal.Decimal('100500')
    assert result.card == cards[0]
    assert result.spent_in == 'XYZ Store'
    assert result.spent_at == datetime.datetime.strptime('25.12.21 14:30', '%d.%m.%y %H:%M')