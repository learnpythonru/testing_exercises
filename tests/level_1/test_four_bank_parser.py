import datetime
from decimal import Decimal

import pytest

from functions.level_1.four_bank_parser import (BankCard, Expense,
                                                parse_ineco_expense)


@pytest.fixture
def result_expenses() -> list[Expense]:
    return [
        Expense(amount=Decimal('2500.00'),
                card=BankCard(last_digits='1234', owner='John Doe'),
                spent_in='Magnit',
                spent_at=datetime.datetime(2023, 11, 18, 13, 31)),
        Expense(amount=Decimal('1200.50'),
                card=BankCard(last_digits='5678', owner='Jane Smith'),
                spent_in='Walmart',
                spent_at=datetime.datetime(2024, 1, 19, 15, 45)),
        Expense(amount=Decimal('0'),
                card=BankCard(last_digits='5678', owner='Jane Smith'),
                spent_in='Wildberries',
                spent_at=datetime.datetime(2024, 1, 19, 15, 45)),
    ]


@pytest.mark.parametrize('sms_index, expected_result_index', [
    (0, 0),
    (1, 1),
    (3, 2),
])
def test__parse_ineco_expense(sms_index, expected_result_index,
                              bank_card_list, sms_list, result_expenses):
    assert parse_ineco_expense(sms_list[sms_index],
                               bank_card_list) == result_expenses[expected_result_index]


@pytest.mark.parametrize('sms_index', [
    2,
])
def test__parse_ineco_expense__with_error(sms_index, sms_list, bank_card_list):
    with pytest.raises(IndexError):
        parse_ineco_expense(sms_list[sms_index], bank_card_list)
