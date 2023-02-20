from functions.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense(sms: SmsMessage, cards: list[BankCard], expense: Expense):
    assert parse_ineco_expense(sms, cards) == expense
