import pytest
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import decimal
import random
import datetime
from datetime import datetime


@pytest.fixture
def create_expenses():

    def create_expense(amount, currency, card_last_digits, card_owner, spent_in, spent_at, category):

        expense = Expense(
            amount=decimal.Decimal(amount),
            currency=Currency(currency).value,
            card=BankCard(last_digits=card_last_digits, owner=card_owner),
            spent_in=spent_in,
            spent_at=datetime.strptime(spent_at, '%d.%m.%Y'),
            category=category
        )
        return expense
    yield create_expense


@pytest.fixture
def random_trigger():
    triggers = (
        "asador", "julis", "doc", "set", "bastard",
        "chinar", "sas", "green apple", "meat house", "clean house",
        "apple.com/bill", "leetcode.com", "zoom.us", "netflix",
        "farm", "pharm", "alfa-pharm", "maname",
        "tomsarkgh", "moscow cinema", "kino park", "cinema galleria",
        "gg platform", "www.taxi.yandex.ru", "bolt.eu", "yandex go"
    )
    trigger = random.choice(triggers)
    return trigger


@pytest.fixture
def random_delimeter():
    allowed_delimiters = (" ", ",", ".", "-", "/", "\\")
    delimeter = random.choice(allowed_delimiters)
    return delimeter
