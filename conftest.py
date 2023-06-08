import pytest
from functions.level_1_7.models import Expense
from datetime import datetime

@pytest.fixture
def expense():
    return Expense(
        amount=100,
        currency='RUB',
        card='1234',
        spent_in='Megafon',
        spent_at=datetime(2023, 6, 1, 0, 0),
        category='ONLINE_SUBSCRIPTIONS'
    )

@pytest.fixture
def history(expense):
    return [
        expense,
        Expense(amount=100, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 2, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
        Expense(amount=100, currency='RUB', card='1234', spent_in='Megafon', spent_at=datetime(2023, 3, 1, 0, 0), category='ONLINE_SUBSCRIPTIONS'),
    ]
