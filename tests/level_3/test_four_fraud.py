import datetime
from decimal import Decimal

from functions.level_3.four_fraud import find_fraud_expenses
from functions.level_3.models import (BankCard, Currency, Expense,
                                      ExpenseCategory)


def test__find_fraud_expenses__success(expenses_list):
    expected_data = [
        Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                category=ExpenseCategory.TRANSPORT),
        Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                category=ExpenseCategory.TRANSPORT),
        Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                category=ExpenseCategory.TRANSPORT),
        Expense(amount=Decimal('722.28'), currency=Currency.EUR,
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='leetcode.com', spent_at=datetime.datetime(2023, 12, 9, 17, 53, 28, 127368),
                category=ExpenseCategory.TRANSPORT),
    ]
    assert find_fraud_expenses(expenses_list) == expected_data


def test__find_fraud_expenses__with_empty_list():
    assert find_fraud_expenses([]) == []


def test__find_fraud_expenses__with_no_fraud_in_expenses_list(expenses_list):
    assert find_fraud_expenses(expenses_list[:15]) == []
