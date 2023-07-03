import pytest
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import decimal
import random
from datetime import datetime
from functions.level_2.two_students import Student
from unittest.mock import patch
import os
import configparser
from faker import Faker

@pytest.fixture
def create_expenses():
    def make_expense(
            amount: str | None = None,
            currency: str | None = None,
            card_last_digits: str | None = None,
            card_owner: str | None = None,
            spent_in: str | None = None,
            spent_at: str | None = None,
            category: ExpenseCategory | None = None
            ):
        amount = amount or '200'
        currency = currency or 'RUB'
        card_last_digits = card_last_digits or '1402'
        card_owner = card_owner or 'vasin vasya'
        spent_in = spent_in or 'sas'
        spent_at = spent_at or '15.05.2023'
        category = category or None

        return Expense(
            amount=decimal.Decimal(amount),
            currency=Currency(currency),
            card=BankCard(last_digits=card_last_digits, owner=card_owner),
            spent_in=spent_in,
            spent_at=datetime.strptime(spent_at, '%d.%m.%Y'),
            category=category
        )
    return make_expense


@pytest.fixture
def make_expenses_for_one_day(create_expenses):
    def inner(amounts: list[str], spent_at: str):
        return [create_expenses(amount=amount, spent_at=spent_at) for amount in amounts]
    return inner


@pytest.fixture
def random_trigger():
    triggers = (
        "asador", "julis", "doc", "set", "bastard",
        "chinar", "sas", "green apple", "meat house", "clean house",
        "apple.com/bill", "leetcode.com", "zoom.us", "netflix",
        "farm", "pharm", "alfa-pharm", "maname",
        "tomsarkgh", "moscow cinema", "kino park", "cinema galleria",
        "gg platform", "www.taxi.yandex.ru", "bolt.eu", "yandex go"
    )
    trigger = random.choice(triggers)
    return trigger


@pytest.fixture
def random_delimeter():
    allowed_delimiters = (" ", ",", ".", "-", "/", "\\")
    delimeter = random.choice(allowed_delimiters)
    return delimeter


@pytest.fixture
def make_tg_account():
    fake = Faker()
    tg_account = fake.profile()["username"]
    return tg_account


@pytest.fixture
def make_student():
    fake = Faker()
    def inner(first_name: str | None = None,
              last_name: str | None = None,
              telegram_account: str | None = None):
        return Student(
            first_name=first_name or fake.first_name(),
            last_name=last_name or fake.last_name(),
            telegram_account=telegram_account or f"@{fake.first_name()[0]}{fake.last_name()}"
            )
    return inner

@pytest.fixture
def create_students(make_student):
    def inner(telegram_accounts=list[str]):
        return [make_student(telegram_account=tg_account) for tg_account in telegram_accounts]
    return inner


@pytest.fixture
def random_choice_mock():
    with patch('functions.level_2.three_promocodes.random.choice') as random_choice_mock:
        yield random_choice_mock


@pytest.fixture
def config_mock():
    with patch('functions.level_2.five_extra_fields.configparser.ConfigParser.__getitem__') as configparser_getitem_mock:
        yield configparser_getitem_mock

@pytest.fixture
def make_lines():
    def inner(lines: list[str] | None = None):
        lines = lines or ["1st line.\n", "2st line.\n", "3st line."]
        return lines
    return inner


@pytest.fixture
def create_test_file():
    path_to_fail = 'test.txt'
    with open(path_to_fail, "w", encoding="utf-8") as file:
        file.writelines(["1st line.\n", "#2st line.\n", "3st line."])
    yield path_to_fail
    if os.path.isfile(path_to_fail):
        os.remove(path_to_fail)


@pytest.fixture
def config():
    example = 'example.ini'
    config = configparser.ConfigParser()
    config["tool:app-config"] = {}
    config["tool:app-config"]['example'] = '1'

    with open(example, 'w') as configfile:
        config.write(configfile)
    yield example
    if os.path.isfile(example):
        os.remove(example)

@pytest.fixture
def make_config():
    def inner(section: str | None = None,
              field_name: str | None = None,
              field_value: str | None = None):
        example = 'config.ini'
        config = configparser.ConfigParser()
        section = section or "section"
        config[section] = {}
        field_name = field_name or "field_name"
        field_value = field_value or "field_value_1: 1 \n field_value_2: 2 \n field_value_3: 3"
        config[section][field_name] = field_value

        with open(example, 'w') as configfile:
            config.write(configfile)
        return example

    yield inner
    if os.path.isfile('config.ini'):
        os.remove('config.ini')

