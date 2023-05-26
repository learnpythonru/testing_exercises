from functions.level_1_5.two_square_equation import solve_square_equation

def test_solve_square_equation_if_discriminant_is_negatibe():
    assert solve_square_equation(1.0, 1.0, 1.0) == (None, None)

def test_solve_square_equation_if_discriminant_is_positive():
    assert solve_square_equation(1.0, -3.0, 2.0) == (1.0, 2.0)



