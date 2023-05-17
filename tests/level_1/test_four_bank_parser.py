from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
from datetime import datetime

def test_parse_ineco_expense():
    message = SmsMessage('100 руб, *1234 12.04.23 16:00 nenaprasno.ru authcode 0000', "Tinkoff", datetime.now())
    cards = [BankCard('1234', 'KONSTANTIN MISHAKOV'), BankCard('5678', 'KONSTANTIN MISHAKOV')]

    assert parse_ineco_expense(message, cards)
     
