import pytest
import datetime


@pytest.fixture()
def verb_male():
    yield "verb_male"

@pytest.fixture()
def verb_female():
    yield "verb_female"


@pytest.fixture
def gender_male():
    return "male"

@pytest.fixture
def gender_female():
    return "female"


@pytest.fixture
def random_symbols():
    return "4w5rgt"
