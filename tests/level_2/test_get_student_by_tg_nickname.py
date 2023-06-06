from functions.level_2.two_students import get_student_by_tg_nickname, Student
import pytest


def test__get_student_by_tg_nickname__is_ok_three_params(telegram_username1, students, student1):
    assert get_student_by_tg_nickname(telegram_username1, students) is student1


def test__get_student_by_tg_nickname__first_elem_of_list(telegram_username1, students):
    assert get_student_by_tg_nickname(telegram_username1, students) is students[0]


def test__get_student_by_tg_nickname__is_None(telegram_username2, students):
    assert get_student_by_tg_nickname(telegram_username2, students) is None