from functions.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense(sms_message, list_bank_cards, expense):
    assert parse_ineco_expense(sms_message, list_bank_cards) == expense
