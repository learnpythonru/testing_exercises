from functions.level_1_7.four_fraud import find_fraud_expenses

def test__four_fraud__no_expenses_met_fraud_signs_criteria(create_expenses):

    history_expense_1 = create_expenses('300', 'USD', '1401', 'dashina dasha', "netflix",
                                        '18.04.2023', "")
    history_expense_2 = create_expenses('300', 'EUR', '1400', 'dashin papa', "netflix",
                                        '16.04.2023', "")
    history_expense_3 = create_expenses('300', 'EUR', '1402', 'dashina mama', "netflix",
                                        '16.04.2023', "")
    history_expense_4 = create_expenses('5001', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '16.05.2023', "")
    history_expense_5 = create_expenses('300', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '15.05.2023', "")
    history_expense_6 = create_expenses('300', 'RUB', '0808', 'vasin vasya', "maname",
                                        '16.05.2023', "")
    
    history_expenses = [
        history_expense_1, history_expense_2, history_expense_3, history_expense_4,
        history_expense_5, history_expense_6,
        ]

    fraudulent_expenses = []

    assert find_fraud_expenses(history_expenses) == fraudulent_expenses


def test__four_fraud__return_list_of_expenses_met_fraud_signs_criteria(create_expenses):

    history_expense_1 = create_expenses('300', 'USD', '1401', 'dashina dasha', "netflix",
                                        '16.04.2023', "")
    history_expense_2 = create_expenses('300', 'EUR', '1400', 'dashin papa', "netflix",
                                        '16.04.2023', "")
    history_expense_3 = create_expenses('300', 'EUR', '1402', 'dashina mama', "netflix",
                                        '16.04.2023', "")
    history_expense_4 = create_expenses('5001', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '16.05.2023', "")
    history_expense_5 = create_expenses('300', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '15.05.2023', "")
    history_expense_6 = create_expenses('300', 'RUB', '0808', 'vasin vasya', "maname",
                                        '16.05.2023', "")
    
    history_expenses = [
        history_expense_1, history_expense_2, history_expense_3, history_expense_4,
        history_expense_5, history_expense_6,
        ]

    fraudulent_expenses = [history_expense_1, history_expense_2, history_expense_3, ]

    assert find_fraud_expenses(history_expenses) == fraudulent_expenses
