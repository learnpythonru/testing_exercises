from functions.level_1_5.two_square_equation import solve_square_equation


def test__solve_square_equation__no_roots():
    assert solve_square_equation(1.0, 0.0, 1.0) == (None, None)

def test__solve_square_equation__one_root():
    assert solve_square_equation(1, -2, 1) == (1.0, 1.0)

def test__solve_square_equation__two_roots():
    assert solve_square_equation(1, -3, 2) == (1.0, 2.0)

def test__solve_square_equation__linear():
    assert solve_square_equation(0, 2, -1) == (0.5, None)
