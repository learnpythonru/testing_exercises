import datetime
from _decimal import Decimal

import pytest

from functions.four_bank_parser import BankCard, Expense, SmsMessage


@pytest.fixture
def verb_male_value():
    return "Делал"


@pytest.fixture
def verb_female_value():
    return "Делала"


@pytest.fixture
def verb_female_value():
    return "Делала"


@pytest.fixture
def date_str_tomorrow():
    return "tomorrow"


@pytest.fixture
def date_str_today():
    return "today"


@pytest.fixture
def valid_str_time_midday():
    return "12:00"


@pytest.fixture
def datetime_tomorrow_midday():
    date = datetime.date.today()
    return datetime.datetime(
        date.year,
        date.month,
        date.day + 1,
        12,
        0,
    )


@pytest.fixture
def datetime_today_midday():
    date = datetime.date.today()
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        12,
        0,
    )


@pytest.fixture
def hostname_value():
    return "https://market.yandex.ru"


@pytest.fixture
def relative_url_value():
    return "catalog"


@pytest.fixture
def get_params_value():
    return {
        "product_id": "1",
        "color": "red"
    }


@pytest.fixture
def url_with_params():
    return "https://market.yandex.ru/catalog?product_id=1&color=red"


@pytest.fixture
def url_without_params():
    return "https://market.yandex.ru/catalog"


@pytest.fixture
def valid_ineco_expense_sms_text():
    return "10000 RUR, 5555444433332222 18.02.23 21:15 ZOO_BAR authcode 3456"


@pytest.fixture
def sms_message(valid_ineco_expense_sms_text):
    return SmsMessage(
        text=valid_ineco_expense_sms_text,
        author="ARTEM",
        sent_at=datetime.datetime.now()
    )


@pytest.fixture
def bank_cards():
    return [
        BankCard(last_digits="1111", owner="ARTEM"),
        BankCard(last_digits="2222", owner="CAT"),
    ]


@pytest.fixture
def expense():
    return Expense(
        amount=Decimal('10000'),
        card=BankCard(last_digits="2222", owner="CAT"),
        spent_in="ZOO_BAR",
        spent_at=datetime.datetime(2023, 2, 18, 21, 15),
    )


@pytest.fixture
def long_title():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
           "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum " \
           "dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui " \
           "officia deserunt mollit anim id est laborum."


@pytest.fixture
def long_title_with_brackets():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
           "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum " \
           "dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui " \
           "officia deserunt mollit anim id est laborum.(9)"


@pytest.fixture
def short_title():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit"


@pytest.fixture
def short_title_with_brackets():
    return "Copy of Lorem ipsum dolor sit amet, consectetur adipiscing elit (5)"


@pytest.fixture
def copy_of_short_title():
    return "Copy of Lorem ipsum dolor sit amet, consectetur adipiscing elit"


@pytest.fixture
def short_title_with_brackets_copy():
    return "Copy of Lorem ipsum dolor sit amet, consectetur adipiscing elit (6)"
