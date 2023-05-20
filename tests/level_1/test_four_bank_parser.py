from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
from datetime import datetime
from decimal import Decimal


def test_parse_ineco_expense():
    message = SmsMessage('99.99 руб, *1234 12.04.23 16:00 nenaprasno.ru authcode 0000', "Tinkoff", datetime.now())
    cards = [BankCard('1234', 'KONSTANTIN MISHAKOV'), BankCard('5678', 'KONSTANTIN MISHAKOV')]
    expense = Expense(
        amount=Decimal("99.99"),
        card=cards[0],
        spent_in="nenaprasno.ru",
        spent_at=datetime.strptime("12.04.23 16:00", "%d.%m.%y %H:%M"),
        )

    result = parse_ineco_expense(message, cards)

    assert result == expense
     