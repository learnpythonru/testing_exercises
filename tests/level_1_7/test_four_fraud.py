from functions.level_1_7.four_fraud import find_fraud_expenses

def test__four_fraud__no_fraud_expenses_with_less_then_three_identical_params(create_expenses):

    history_expense_1 = create_expenses(amount='300', spent_in="netflix", spent_at='18.04.2023')
    history_expense_2 = create_expenses(amount='300', spent_in="netflix", spent_at='16.04.2023')
    history_expense_3 = create_expenses(amount='300', spent_in="netflix", spent_at='16.04.2023')
    history_expense_4 = create_expenses(amount='350', spent_in="netflix", spent_at='16.05.2023')
    history_expense_5 = create_expenses(amount='300', spent_in="maname", spent_at='16.05.2023')
    
    history_expenses = [
        history_expense_1, history_expense_2, history_expense_3, history_expense_4,
        history_expense_5
        ]

    fraudulent_expenses = []

    assert find_fraud_expenses(history_expenses) == fraudulent_expenses


def test__four_fraud__no_fraud_expenses_with_more_then_three_identical_params_but_amount_more_5000(create_expenses):

    history_expense_1 = create_expenses(amount='5001', spent_in="netflix", spent_at='16.04.2023')
    history_expense_2 = create_expenses(amount='5001', spent_in="netflix", spent_at='16.04.2023')
    history_expense_3 = create_expenses(amount='5001', spent_in="netflix", spent_at='16.04.2023')
    history_expense_4 = create_expenses(amount='5001', spent_in="netflix", spent_at='16.05.2023')

    history_expenses = [
        history_expense_1, history_expense_2, history_expense_3, history_expense_4
        ]

    fraudulent_expenses = []

    assert find_fraud_expenses(history_expenses) == fraudulent_expenses


def test__four_fraud__return_expenses_with_three_identical_params_and_amount_less_5000(create_expenses):

    history_expense_1 = create_expenses(amount='300', spent_in="netflix", spent_at='16.04.2023')
    history_expense_2 = create_expenses(amount='300', spent_in="netflix", spent_at='16.04.2023')
    history_expense_3 = create_expenses(amount='300', spent_in="netflix", spent_at='16.04.2023')
    history_expense_4 = create_expenses(amount='400', spent_in="netflix", spent_at='16.05.2023')
    history_expense_5 = create_expenses(amount='300', spent_in="netflix", spent_at='15.05.2023')
    history_expense_6 = create_expenses(amount='300', spent_in="maname", spent_at='16.05.2023')

    history_expenses = [
        history_expense_1, history_expense_2, history_expense_3, history_expense_4,
        history_expense_5, history_expense_6,
        ]

    fraudulent_expenses = [history_expense_1, history_expense_2, history_expense_3, ]

    assert find_fraud_expenses(history_expenses) == fraudulent_expenses
