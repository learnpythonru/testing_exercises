from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal


def test_parse_ineco_expense():
    assert parse_ineco_expense( \
        SmsMessage("1000 00, 1234123412341234 12.11.21 15:30 300 authcode 10", "auth", datetime.datetime(2023, 1, 1)),
        [BankCard("3412", "Mr V"), BankCard("1234", "Ms V")]) == Expense(amount=decimal.Decimal('1000'),
                                                                         card=BankCard(last_digits='1234',
                                                                                       owner='Ms V'), spent_in='300',
                                                                         spent_at=datetime.datetime(2021, 11, 12, 15,
                                                                                                    30))
