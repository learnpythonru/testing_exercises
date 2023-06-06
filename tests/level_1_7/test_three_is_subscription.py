from functions.level_1_7.three_is_subscription import is_subscription
from functions.level_1_7.models import Expense
import pytest
from datetime import datetime


@pytest.mark.parametrize(
    "expense, history, expected_result",
    [
        (
            Expense(amount=100, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 6, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
            [
                Expense(amount=100, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 1, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
                Expense(amount=200, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 2, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
                Expense(amount=300, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 3, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
                Expense(amount=400, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 4, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
                Expense(amount=500, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 5, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
            ],
            True
        ),
        (
            Expense(amount=500, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 6, 5, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
            [
                Expense(amount=500, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 1, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
                Expense(amount=500, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 2, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
                Expense(amount=500, currency='RUB', card='1234', spent_in='Cofeshop', spent_at=datetime(2023, 3, 1, 0, 0), category='BAR_RESTAURANT'),
            ],
            False
        ),
    ]
)
def test__is_subscription(expense, history, expected_result):
    assert is_subscription(expense, history) == expected_result




                




















# def test__is_subscription(expense, history)