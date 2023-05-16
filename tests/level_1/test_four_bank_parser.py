from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal

def test_parse_ineco_expense():
    assert parse_ineco_expense(
        SmsMessage('1000.001 768.987 78.090, 240808 15.05.23 12:00 14:15 authcode ERS125', 
                   'Petya', (2023, 5, 15, 14, 15, 44)), 
        [BankCard('0808', 'vasya')]
                   ) == Expense(amount=decimal.Decimal('768.987'), card=BankCard(last_digits='0808', owner='vasya'), 
                                spent_in='14:15', spent_at=datetime.datetime(2023, 5, 15, 12, 0))
