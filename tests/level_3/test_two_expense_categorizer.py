import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category


@pytest.mark.parametrize('index, expected_result', [
    (0, ExpenseCategory.SUPERMARKET),
    (1, ExpenseCategory.MEDICINE_PHARMACY),
    (-1, ExpenseCategory.ONLINE_SUBSCRIPTIONS),
    (5, ExpenseCategory.ONLINE_SUBSCRIPTIONS),
    (-2, None),
])
def test__guess_expense_category__succes(expenses_list, index, expected_result):
    assert guess_expense_category(expenses_list[index]) == expected_result
