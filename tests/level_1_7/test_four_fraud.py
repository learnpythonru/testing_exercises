from functions.level_1_7.four_fraud import find_fraud_expenses
from functions.level_1_7.models import Expense, BankCard, ExpenseCategory, Currency
from decimal import Decimal
from datetime import datetime
import pytest

def test__find_fraud_expenses__if_get_more_than_max_amount():
    history = [
        Expense(
            amount=Decimal('5000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('5001.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('6001.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),

    ]

    expected_fraud_transactions = []

    fraud_transactions = find_fraud_expenses(history)
    assert fraud_transactions == expected_fraud_transactions


def test__find_fraud_expenses__if_get_less_than_min_chain_length():
    history = [
        Expense(
            amount=Decimal('1000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('2000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
    ]

    fraud_transactions = find_fraud_expenses(history)
    assert fraud_transactions == []

@pytest.mark.xfail(reason='Incorrect work of function') # Думаю функция реализована неправильно. Но может я не разобрался просто.
def test__find_fraud_expenses__if_get_multiple_fraud_chains():
    history = [
        Expense(
            amount=Decimal('1000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('2000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('3000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('4000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
    ]

    expected_fraud_transactions = [
        Expense(
            amount=Decimal('1000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('2000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('3000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal('4000.00'),
            currency=Currency.RUB,
            card=BankCard(last_digits='1234', owner='Alexandr'),
            spent_in='The best drinking bar',
            spent_at=datetime(2023, 6, 4, 23, 0, 0),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
    ]

    fraud_transactions = find_fraud_expenses(history)
    assert fraud_transactions == expected_fraud_transactions


