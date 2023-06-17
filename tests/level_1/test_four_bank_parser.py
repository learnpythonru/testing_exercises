from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
from datetime import datetime
from decimal import Decimal
import pytest


@pytest.mark.parametrize(
        'message, cards, expected_result',
        [
            (
                SmsMessage('99.99 руб, *1234 12.04.23 16:00 nenaprasno.ru authcode 0000', "Tinkoff", datetime.now()),
                [BankCard('1234', 'KONSTANTIN MISHAKOV'), BankCard('5678', 'KONSTANTIN MISHAKOV')],
                Expense(
                    amount=Decimal("99.99"),
                    card=[BankCard('1234', 'KONSTANTIN MISHAKOV'), BankCard('5678', 'KONSTANTIN MISHAKOV')][0],
                    spent_in="nenaprasno.ru",
                    spent_at=datetime.strptime("12.04.23 16:00", "%d.%m.%y %H:%M"),
                ),
            ),
        ],
)
def test__parse_ineco_expense_success(message, cards, expected_result):
    assert parse_ineco_expense(message, cards) == expected_result


@pytest.mark.parametrize(
        'message, cards, exception_type',
        [
            (
                SmsMessage('99.99 руб, *1234 12.04.23 16:00 nenaprasno.ru authcode 0000', "Tinkoff", datetime.now()),
                [BankCard('5678', 'KONSTANTIN MISHAKOV')],
                IndexError,
            ),
        ],
)
def test__parse_ineco_expense__exception(message, cards, exception_type):
    with pytest.raises(exception_type):
        parse_ineco_expense(message, cards)
