from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal
from typing import NamedTuple


def test_parse_ineco_expense():
    text = "112.3 $, 40004234 13.05.23 17:23 Shop_name authcode jhtfj"
    author = "Masha"
    sent_at = datetime.datetime.now().time()
    # Входное значение для функции  
    sms= SmsMessage(text, author, sent_at)

    bank_card1 = BankCard(last_digits='0123', owner= 'User1')
    bank_card2 = BankCard(last_digits = '4234', owner = 'User2')
    #   Входное значение для функции  
    cards = [bank_card1, bank_card2]

    expense_result=Expense(amount = decimal.Decimal('112.3'), card = BankCard(last_digits ='4234', owner ='User2'), spent_in = 'Shop_name', spent_at = datetime.datetime(2023, 5, 13, 17, 23))
    assert parse_ineco_expense(sms, cards) == expense_result
    
<<<<<<< HEAD
=======
    Expense_result = Expense(amount, card, spend_in, spent_at)

    assert parse_ineco_expense(sms, cards) == Expense_result
    assert type(parse_ineco_expense(sms, cards)) == Expense

>>>>>>> main
