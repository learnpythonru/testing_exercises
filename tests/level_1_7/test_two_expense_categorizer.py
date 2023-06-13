from functions.level_1_7.two_expense_categorizer import guess_expense_category
from functions.level_1_7.models import Expense, ExpenseCategory
import pytest
from datetime import datetime

@pytest.mark.parametrize(
    'expense, ExpenseCategory',
    [
        (Expense(amount=10000, currency='RUB', card='1234', spent_in='Bastard place', spent_at=datetime(2023, 6, 1, 0, 0), category=None),
        ExpenseCategory.BAR_RESTAURANT),
        (Expense(amount=1000, currency='RUB', card='1234', spent_in='clean house', spent_at=datetime(2023, 6, 1, 0, 0), category=None),
        ExpenseCategory.SUPERMARKET),
        (Expense(amount=10, currency='USD', card='1234', spent_in='Netflix', spent_at=datetime(2023, 6, 1, 0, 0), category=None),
        ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        (Expense(amount=3000, currency='RUB', card='1234', spent_in='Wonder pharm', spent_at=datetime(2023, 6, 1, 0, 0), category=None),
        ExpenseCategory.MEDICINE_PHARMACY),
        (Expense(amount=2000, currency='RUB', card='1234', spent_in='kino park', spent_at=datetime(2023, 6, 1, 0, 0), category=None),
        ExpenseCategory.THEATRES_MOVIES_CULTURE),
        (Expense(amount=2000, currency='RUB', card='1234', spent_in='www.taxi.yandex.ru', spent_at=datetime(2023, 6, 1, 0, 0), category=None),
        ExpenseCategory.TRANSPORT),
        (Expense(amount=5000, currency='RUB', card='1234', spent_in='Y Ashota', spent_at=datetime(2023, 6, 1, 0, 0), category=None),
        None),
    ]
)
def test__guess_expense_category(expense:Expense, ExpenseCategory:ExpenseCategory | None)->ExpenseCategory | None:
    assert guess_expense_category(expense) == ExpenseCategory