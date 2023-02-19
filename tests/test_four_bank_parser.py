import pytest

from functions.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


@pytest.mark.parametrize(
    "sms, cards, expected_expense",
    [
        (
            pytest.lazy_fixture("sms_message"),
            pytest.lazy_fixture("bank_cards"),
            pytest.lazy_fixture("expense"),
        ),
    ],
)
def test_parse_ineco_expense(sms: SmsMessage, cards: list[BankCard], expected_expense: Expense):
    assert parse_ineco_expense(sms, cards) == expected_expense
