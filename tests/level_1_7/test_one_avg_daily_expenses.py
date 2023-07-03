from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses
import pytest

def test__calculate_average_daily_expenses__success(create_expenses):
    expense_1 = create_expenses(amount='500', spent_at='15.05.2023')
    expense_2 = create_expenses(amount='100', spent_at='16.05.2023')
    expense_3 = create_expenses(amount='700', spent_at='15.05.2023')
    assert calculate_average_daily_expenses([expense_1, expense_2, expense_3]) == 650


def test__calculate_average_daily_expenses__success_return_amount(create_expenses):
    expense_1 = create_expenses(amount='500', spent_at='15.05.2023')
    assert calculate_average_daily_expenses([expense_1]) == 500


@pytest.mark.parametrize(('expenses, expected'), [
    pytest.param(
        [
            (['200', '400'], '15.05.2023'),
            (['600', '800'], '16.05.2023'),
        ], 1000),
    pytest.param(
        [
            (['200', '400'], '15.05.2023'),
            (['500'], '16.05.2023'),
        ], 550)
])

def test__calculate_average_daily_expenses__success_2(make_expenses_for_one_day, expenses, expected):
    total_expenses = []
    for amounts, spent_at in expenses:
        total_expenses.extend(make_expenses_for_one_day(amounts=amounts, spent_at=spent_at))

    assert calculate_average_daily_expenses(total_expenses) == expected
