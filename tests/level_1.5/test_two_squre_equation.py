from functions.level_1_5.two_square_equation import solve_square_equation
import pytest


def test__solve_square_equation__normal_input():
    assert solve_square_equation(1, 2, -3) == (-3.0, 1.0)


def test__solve_square_equation__discriminant_below_zero():
    assert solve_square_equation(1, 1, 1) == (None, None)


def test__solve_square_equation__a_is_zero_b_is_zero():
    assert solve_square_equation(0, 0, 1) == (None, None)


def test__solve_square_equation__a_is_zero():
    assert solve_square_equation(0, -2, 2) == (1.0, None)


@pytest.mark.xfail(reason='should be only one root for the equation when dicriminant is zero')
def test__solve_square_equation__discriminant_is_zero():
    assert solve_square_equation(1, 2, 1) == (-1.0, None)
