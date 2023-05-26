from functions.level_1_5.two_square_equation import solve_square_equation
import pytest


def test__solve_square_equation__if_discriminant_is_negative():
    assert solve_square_equation(1.0, 1.0, 1.0) == (None, None)


def test__solve_square_equation__if_discriminant_is_positive():
    assert solve_square_equation(1.0, -3.0, 2.0) == (1.0, 2.0)


@pytest.mark.xfail
def test__solve_square_equation__if_discriminant_is_equal_to_zero():
    assert solve_square_equation(1.0, -2.0, 1.0) == (1, None)


def test__solve_square_equation__if_square_coefficient_is_equal_to_zero():
    assert solve_square_equation(0, 2.0, 1) == (-0.5, None)


def test__solve_square_equation__if_square_coefficient_and__linear_coefficients_are_equal_to_zero():
    assert solve_square_equation(0, 0, 1) == (None, None)