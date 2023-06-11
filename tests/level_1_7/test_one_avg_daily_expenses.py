from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__two_amounts_for_one_day_one_for_different_day(create_expenses, random_trigger):
    expense_1 = create_expenses('200', 'RUB', '0808', 'vasin vasya', random_trigger,
                                '15.05.2023', 'SUPERMARKET')
    expense_2 = create_expenses('400', 'USD', '1401', 'dashina dasha', random_trigger,
                                '16.05.2023', 'BAR_RESTAURANT')
    expense_3 = create_expenses('700', 'EUR', '1401', 'dashina dasha', random_trigger,
                                '15.05.2023', "")

    assert calculate_average_daily_expenses([expense_1, expense_2, expense_3]) == 650
