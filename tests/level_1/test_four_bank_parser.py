from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal
from typing import NamedTuple


def test_parse_ineco_expense():
    raw_sum = "112.3 $"
    raw_card = "40004234"
    raw_date ="13.05.23" 
    raw_time = "17:23" 
    spend_in = "Shop_name"

    text = raw_sum + ', ' + raw_card + " " + raw_date + " " + raw_time + " " + spend_in + " authcode "+"jhtfj"
    author = "Masha"
    sent_at = datetime.datetime.now().time()
# Входное значение для функции  
    sms= SmsMessage(text, author, sent_at)

    last_digits = '0123'
    owner = 'User1'
    BankCard1 = BankCard(last_digits, owner)

    last_digits = '4234'
    owner = 'User2'
    BankCard2 = BankCard(last_digits, owner)
# Входное значение для функции  
    cards = [BankCard1, BankCard2]

    raw_sum, raw_details = text.split(', ')
    raw_details = raw_details.split(' authcode ')[0]
    raw_card, raw_date, raw_time, spend_in = raw_details.split(' ', maxsplit=3)
    amount=decimal.Decimal(raw_sum.split(' ')[-2])
    card=[c for c in cards if c.last_digits == raw_card[-4:]][0]
    spent_at=datetime.datetime.strptime(f'{raw_date} {raw_time}', '%d.%m.%y %H:%M')
    
    Expense_result = Expense(amount, card, spend_in, spent_at)

    assert parse_ineco_expense(sms, cards) == Expense_result
    assert type(parse_ineco_expense(sms, cards)) == Expense

