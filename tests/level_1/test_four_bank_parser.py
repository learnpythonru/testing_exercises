from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense
import datetime
import decimal
import pytest

def test__parse_ineco_expense__from_normal_input_sms():
    # arrange
    sms = SmsMessage(
        text='1000.001 768.987 78.090, 240808 15.05.23 12:00 14:15 authcode ERS125',
        author='Microkredit_Petya',
        sent_at=datetime.datetime(2023, 5, 15, 14, 15, 44)
        )
    card = BankCard(
        last_digits='0808',
        owner='vasya')

    # act
    expense = parse_ineco_expense(sms, cards=[card])

    # assert
    assert expense.amount == decimal.Decimal('768.987')
    assert expense.card.last_digits == '0808', 'must be equal bank card in bank operation'
    assert expense.card.owner == 'vasya'
    assert expense.spent_in == '14:15'
    assert expense.spent_at == datetime.datetime(2023, 5, 15, 12, 0)


def test__parse_ineco_expense__cards_number_from_sms_is_different_from_bank_card():
    # arrange
    sms = SmsMessage(
        text='1000.001 768.987 78.090, 240809 15.05.23 12:00 14:15 authcode ERS125',
        author='Microkredit_Petya',
        sent_at=datetime.datetime(2023, 5, 15, 14, 15, 44)
        )
    card = BankCard(
        last_digits='0808',
        owner='vasya')

    # act
    with pytest.raises(Exception) as e:
        parse_ineco_expense(sms, cards=[card])
    
    # assert
    assert e.type == IndexError


def test__parse_ineco_expense__no_authcode_in_sms():
    # arrange
    sms = SmsMessage(
        text='1000.001 768.987 78.090, 240808 15.05.23 12:00 14:15',
        author='Microkredit_Petya',
        sent_at=datetime.datetime(2023, 5, 15, 14, 15, 44)
        )
    card = BankCard(
        last_digits='0808',
        owner='vasya')

    # act
    expense = parse_ineco_expense(sms, cards=[card])

    # assert
    assert expense.amount == decimal.Decimal('768.987')
    assert expense.card.last_digits == '0808', 'must be equal bank card in bank operation'
    assert expense.card.owner == 'vasya'
    assert expense.spent_in == '14:15'
    assert expense.spent_at == datetime.datetime(2023, 5, 15, 12, 0)


def test__parse_ineco_expense__just_one_number_in_sms_text():
    # arrange
    sms = SmsMessage(
        text='1000.001, 240808 15.05.23 12:00 14:15',
        author='Microkredit_Petya',
        sent_at=datetime.datetime(2023, 5, 15, 14, 15, 44)
        )
    card = BankCard(
        last_digits='0808',
        owner='vasya')

    # act
    with pytest.raises(Exception) as e:
        parse_ineco_expense(sms, cards=[card])
    
    # assert
    assert e.type == IndexError


def test__parse_ineco_expense__excessive_data_in_spent_in_sms_text():
    # arrange
    sms = SmsMessage(
        text='1000.001 768.987, 240808 15.05.23 12:00 14:15 Goodbye',
        author='Microkredit_Petya',
        sent_at=datetime.datetime(2023, 5, 15, 14, 15, 44)
        )
    card = BankCard(
        last_digits='0808',
        owner='vasya')

    # act
    expense = parse_ineco_expense(sms, cards=[card])

    # assert
    assert expense.spent_in == '14:15 Goodbye'
