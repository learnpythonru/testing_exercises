from functions.level_1_5.two_square_equation import solve_square_equation


def test__salve_square_equation__discriminant_less_than_zero():
    assert solve_square_equation(2.12, 4.5, 8.55) == (None, None)


def test__salve_square_equation__square_coefficient_not_eq_zero():
    assert solve_square_equation(1, 3, 2) == (-2.0, -1.0)


def test__salve_square_equation__square_coef_eq_zero():
    assert solve_square_equation(0, 2, 2) == (-1.0, None)


def test__salve_square_equation__square_linear_eq_zero():
    assert solve_square_equation(0, 0, 2) == (None, None)