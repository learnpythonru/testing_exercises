from functions.level_2.two_students import get_student_by_tg_nickname

#вроде бы тут мокать нечего

def test__get_student_by_tg_nickname__success(create_students):
    tg_students = ['@ivanov', '@petrov', '@sidorov']
    students = create_students(telegram_accounts=tg_students)

    assert get_student_by_tg_nickname('petrov', students) == students[1]


def test__get_student_by_tg_nickname__success_return_first_student_in_students_with_set_tg_account(create_students):
    tg_students = ['@ivanov', 'petrov', 'ivanov']
    students = create_students(telegram_accounts=tg_students)

    assert get_student_by_tg_nickname('ivanov', students) == students[0]


def test__get_student_by_tg_nickname__return_None_no_students_with_set_tg_account(make_student, make_tg_account):
    telegram_username = make_tg_account
    student_1 = make_student()
    student_2 = make_student()
    students = [student_1, student_2]
    assert get_student_by_tg_nickname(telegram_username, students) is None
