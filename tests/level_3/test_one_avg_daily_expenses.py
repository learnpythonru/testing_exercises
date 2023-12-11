import datetime
from decimal import Decimal

from functions.level_3.models import (BankCard, Currency, Expense,
                                      ExpenseCategory)
from functions.level_3.one_avg_daily_expenses import \
    calculate_average_daily_expenses


def test__calculate_average_daily_expenses__succes(expenses_list):
    assert calculate_average_daily_expenses(expenses_list) == Decimal('1639.58')


def test__calculate_average_daily_expenses__with_zero_amounts():
    data = [Expense(amount=Decimal('0.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='doc', spent_at=datetime.datetime(2023, 12, 10, 17, 53, 28, 127676),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('0.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='chinar', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                    category=ExpenseCategory.SUPERMARKET),
            Expense(amount=Decimal('0.00'), currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)]
    assert calculate_average_daily_expenses(data) == Decimal('0.00')


def test__calculate_average_daily_expenses__with_equal_amounts():
    data = [Expense(amount=Decimal('150.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='doc', spent_at=datetime.datetime(2023, 12, 10, 17, 53, 28, 127676),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('150.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='chinar', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                    category=ExpenseCategory.SUPERMARKET),
            Expense(amount=Decimal('150.00'), currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)]
    assert calculate_average_daily_expenses(data) == Decimal('150.00')


def test__calculate_average_daily_expenses__with_equal_dates():
    data = [Expense(amount=Decimal('100.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='doc', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127676),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('50.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='chinar', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                    category=ExpenseCategory.SUPERMARKET),
            Expense(amount=Decimal('150.00'), currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)]
    assert calculate_average_daily_expenses(data) == Decimal('300.00')


def test__calculate_average_daily_expenses__with_negative_amounts():
    data = [Expense(amount=Decimal('-100.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='doc', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127676),
                    category=ExpenseCategory.TRANSPORT),
            Expense(amount=Decimal('-100.00'), currency=Currency.AMD,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='chinar', spent_at=datetime.datetime(2023, 12, 8, 17, 53, 28, 127730),
                    category=ExpenseCategory.SUPERMARKET),
            Expense(amount=Decimal('-150.00'), currency=Currency.RUB,
                    card=BankCard(last_digits='1234', owner='John Doe'),
                    spent_in='zoom.us', spent_at=datetime.datetime(2023, 12, 7, 17, 53, 28, 127785),
                    category=ExpenseCategory.ONLINE_SUBSCRIPTIONS)]
    assert calculate_average_daily_expenses(data) == Decimal('-175.00')
