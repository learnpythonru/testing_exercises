from functions.level_1_5.three_first import NOT_SET
import pytest

#test_first

@pytest.fixture
def items_1():
    return [1, 2, 3]

@pytest.fixture
def items_2():
    return []

@pytest.fixture
def items_3():
    return ''

@pytest.fixture
def items_4():
    return None

@pytest.fixture
def items_5():
    return 0

@pytest.fixture
def default_1():
    return None

@pytest.fixture
def default_2():
    return NOT_SET

@pytest.fixture
def default_3():
    return 'default'

@pytest.fixture
def default_4():
    return 1234

@pytest.fixture
def default_5():
    return (5, 56)

@pytest.fixture
def default_6():
    return 0

@pytest.fixture
def result_1():
    return 1

@pytest.fixture
def result_5():
    return 'd'

@pytest.fixture
def result_6():
    return 'N'
