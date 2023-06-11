from functions.level_1_7.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
import pytest
from functions.level_1_7.models import ExpenseCategory

def test__is_string_contains_trigger__start_with_delimeter_success(random_trigger, random_delimeter):
    original_string = random_delimeter + random_trigger

    assert is_string_contains_trigger(original_string, random_trigger) is True


def test__is_string_contains_trigger__end_with_delimeter_success(random_trigger, random_delimeter):
    original_string = random_trigger + random_delimeter

    assert is_string_contains_trigger(original_string, random_trigger) is True


def test__is_string_contains_trigger__trigger_between_delimeters_success(random_trigger, random_delimeter):
    original_string = random_delimeter + random_trigger + random_delimeter

    assert is_string_contains_trigger(original_string, random_trigger) is True


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
    expense = create_expenses('200', 'RUB', '0808', 'vasin vasya', 'sas',
                              '15.05.2023', "")
    assert guess_expense_category(expense) == ExpenseCategory.SUPERMARKET


def test__guess_expense_category__success(create_expenses, random_delimeter):
    expense_1 = create_expenses('200', 'RUB', '0808', 'vasin vasya', random_delimeter + 'julis',
                                '15.05.2023', "")
    assert guess_expense_category(expense_1) == ExpenseCategory.BAR_RESTAURANT


def test__guess_expense_category__fail_no_trigger_in_Expense_category(create_expenses):
    expense_1 = create_expenses('200', 'RUB', '0808', 'vasin vasya', 'home',
                                '15.05.2023', "")
    assert guess_expense_category(expense_1) is None
