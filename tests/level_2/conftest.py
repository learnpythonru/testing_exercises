import pytest
from functions.level_2.two_students import Student


@pytest.fixture
def name():
    return("{ Something }")

@pytest.fixture
def result1(name):
   return name[2:len(name) - 2]

@pytest.fixture
def name2():
    return("{ Something }")

@pytest.fixture
def result2():
    return "Something"

@pytest.fixture
def student1():
    return Student("Diana", "Ratnikova", "@winterlich_weiss")

@pytest.fixture
def student2():
    return Student("Name", "Last Name", "@nickname")

@pytest.fixture
def student3():
    return Student("wrtgshn", "athbgfs", "nickname")

@pytest.fixture
def students(student1, student2, student3):
    return [student1, student2, student3]

@pytest.fixture
def telegram_username1():
    return "winterlich_weiss"

@pytest.fixture
def telegram_username2():
    return "wshgfhnjtnhg"
