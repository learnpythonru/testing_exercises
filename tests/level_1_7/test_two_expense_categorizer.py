from functions.level_1_7.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
import pytest
from functions.level_1_7.models import ExpenseCategory


@pytest.mark.parametrize(
       "original_string,trigger,expected_result",
       [
           (" asador", "asador", True),
           ("farm,", "farm", True),
           ("\\tomsarkgh-", "tomsarkgh", True),
        ]
)
def test__is_string_contain_trigger__success(original_string, trigger, expected_result):
    assert is_string_contains_trigger(original_string, trigger) is expected_result


@pytest.mark.parametrize(
        "original_string,trigger,expected_result",
        [
            ("home", "asador", False),
            (";asador", "asador", False),
        ],
        ids=[
            "trigger is not in triggers list",
            "not allowed delimeter"
        ]
)
def test__is_string_contains_trigger__fail(original_string, trigger, expected_result):
    assert is_string_contains_trigger(original_string, trigger) is expected_result


def test__guess_expense_category__success(create_expenses):
    expense = create_expenses(spent_in='sas')
    assert guess_expense_category(expense) == ExpenseCategory.SUPERMARKET


def test__guess_expense_category__success_with_random_delimeter(create_expenses, random_delimeter):
    expense_1 = create_expenses(spent_in=random_delimeter+'julis')
    assert guess_expense_category(expense_1) == ExpenseCategory.BAR_RESTAURANT


def test__guess_expense_category__fail_no_trigger_in_Expense_category(create_expenses):
    expense_1 = create_expenses(spent_in='home')
    assert guess_expense_category(expense_1) is None
