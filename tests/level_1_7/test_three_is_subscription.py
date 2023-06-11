from functions.level_1_7.three_is_subscription import is_subscription

def test__three_is_subscription__three_the_same_destination_expenses_per_month_return_true(create_expenses):

    expense_for_check = create_expenses('200', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '15.05.2023', "")
    history_expense_1 = create_expenses('300', 'USD', '1401', 'dashina dasha', "netflix",
                                        '16.04.2023', "")
    history_expense_2 = create_expenses('700', 'EUR', '1400', 'dashin papa', "netflix",
                                        '15.03.2023', "")
    history_expense_3 = create_expenses('700', 'EUR', '1402', 'dashina mama', "netflix",
                                        '15.06.2023', "")
    history_of_expenses = [history_expense_1, history_expense_2, history_expense_3]

    assert is_subscription(expense_for_check, history_of_expenses) is True


def test__three_is_subscription__less_then_three_the_same_destination_expenses_return_false(create_expenses):

    expense_for_check = create_expenses('200', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '15.05.2023', "")
    history_expense_1 = create_expenses('300', 'USD', '1401', 'dashina dasha', "netflix",
                                        '16.04.2023', "")
    history_expense_2 = create_expenses('700', 'EUR', '1400', 'dashin papa', "zoom.us",
                                        '15.03.2023', "")
    history_expense_3 = create_expenses('700', 'EUR', '1402', 'dashina mama', "netflix",
                                        '15.06.2023', "")
    history_of_expenses = [history_expense_1, history_expense_2, history_expense_3]

    assert is_subscription(expense_for_check, history_of_expenses) is False


def test__three_is_subscription__two_expenses_in_one_month_return_false(create_expenses):

    expense_for_check = create_expenses('200', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '15.05.2023', "")
    history_expense_1 = create_expenses('300', 'USD', '1401', 'dashina dasha', "netflix",
                                        '16.04.2023', "")
    history_expense_2 = create_expenses('700', 'EUR', '1400', 'dashin papa', "netflix",
                                        '15.04.2023', "")
    history_expense_3 = create_expenses('700', 'EUR', '1402', 'dashina mama', "netflix",
                                        '15.06.2023', "")
    history_of_expenses = [history_expense_1, history_expense_2, history_expense_3]

    assert is_subscription(expense_for_check, history_of_expenses) is False


def test__three_is_subscription__two_expenses_in_one_month_and_different_destinations_return_false(create_expenses):

    expense_for_check = create_expenses('200', 'RUB', '0808', 'vasin vasya', "netflix",
                                        '15.05.2023', "")
    history_expense_1 = create_expenses('300', 'USD', '1401', 'dashina dasha', "netflix",
                                        '16.04.2023', "")
    history_expense_2 = create_expenses('700', 'EUR', '1400', 'dashin papa', "maname",
                                        '15.04.2023', "")
    history_expense_3 = create_expenses('700', 'EUR', '1402', 'dashina mama', "www.taxi.yandex.ru",
                                        '15.06.2023', "")
    history_of_expenses = [history_expense_1, history_expense_2, history_expense_3]

    assert is_subscription(expense_for_check, history_of_expenses) is False


def test__three_is_subscription___destination_expense_differ_from_history_return_false(create_expenses):

    expense_for_check = create_expenses('200', 'RUB', '0808', 'vasin vasya', "maname",
                                        '15.05.2023', "")
    history_expense_1 = create_expenses('300', 'USD', '1401', 'dashina dasha', "netflix",
                                        '16.04.2023', "")
    history_expense_2 = create_expenses('700', 'EUR', '1400', 'dashin papa', "netflix",
                                        '15.03.2023', "")
    history_expense_3 = create_expenses('700', 'EUR', '1402', 'dashina mama', "netflix",
                                        '15.06.2023', "")
    history_of_expenses = [history_expense_1, history_expense_2, history_expense_3]

    assert is_subscription(expense_for_check, history_of_expenses) is False
