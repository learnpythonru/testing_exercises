import decimal
from datetime import datetime
import pytest
from functions.level_1_7.models import Expense, BankCard, Currency
from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses

@pytest.mark.parametrize(
    'expenses, expected_result',
    [
        (
            [
                Expense(
                    amount=decimal.Decimal('100.00'),
                    currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='Alexandr'),
                    spent_in='Funny Shop',
                    spent_at=datetime(2023, 6, 1, 12, 0, 0, 0),
                    category=None
                ),
                Expense(
                    amount=decimal.Decimal('200.00'),
                    currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='Alexandr'),
                    spent_in='Funny Shop',
                    spent_at=datetime(2023, 6, 1, 13, 0, 0, 0),
                    category=None
                ),
                Expense(
                    amount=decimal.Decimal('300.00'),
                    currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='Alexandr'),
                    spent_in='Funny Shop',
                    spent_at=datetime(2023, 6, 2, 14, 0, 0, 0),
                    category=None
                ),
                Expense(
                    amount=decimal.Decimal('400.00'),
                    currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='Alexandr'),
                    spent_in='Funny Shop',
                    spent_at=datetime(2023, 6, 2, 15, 0, 0, 0),
                    category=None
                ),
            ],
            decimal.Decimal('500.00')
        ),
    ]
)
def test__calculate_average_daily_expenses(expenses, expected_result):
    assert calculate_average_daily_expenses(expenses) == expected_result
