import pytest

from functions.level_2.two_students import get_student_by_tg_nickname, Student

STUDENTS = [
    Student("Ivan", "Ivanov", "@ivan"),
    Student("Petr", "Petrov", None),
]


@pytest.mark.parametrize(
    "telegram_username, expected",
    [
        ("ivan", Student("Ivan", "Ivanov", "@ivan")),
        ("petr", None),
    ],
)
def test__get_student_by_tg_nickname(telegram_username: str, expected: Student):
    assert get_student_by_tg_nickname(telegram_username, STUDENTS) == expected
