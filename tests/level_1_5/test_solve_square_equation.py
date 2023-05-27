from functions.level_1_5.two_square_equation import solve_square_equation
import pytest


def test__solve_square_equation__all_params_zero():
    assert solve_square_equation(0, 0, 0) == (None, None)


def test__solve_square_equation__const_coefficient_zero(): 
    assert solve_square_equation(5, 2, 0) == (-0.4, 0.0)


def test__solve_square_equation__square_coefficient_zero():     
    assert solve_square_equation(0, 2, 10) == (-5.0, None)


def test__solve_square_equation__only_linear_coefficient():
    assert solve_square_equation(0, 2, 0) == (0.0, None)


def test__solve_square_equation__linear_coefficient_zero():
    assert solve_square_equation(4, 0, -16) == (-2.0, 2.0)


def test__solve_square_equation__all_coefficients_int():
    assert solve_square_equation(5, 3, -26) == (-2.6, 2.0)


def test__solve_square_equation__discriminant_below_zero():
    assert solve_square_equation(1, 2, 5) == (None, None)


def test__solve_square_equation__all_coefficients_float():
    assert solve_square_equation(1.1, 2.2, -5.5) == (-3.449489742783178, 1.4494897427831779)


def test__solve_square_equation__not_enougt_params():
    with pytest.raises(TypeError):
        solve_square_equation(0, 0)


def test__solve_square_equation__too_many_params():
    with pytest.raises(TypeError):
        solve_square_equation(5, 2, 0, 9)


def test__solve_square_equation__params_are_string():
    with pytest.raises(TypeError):
        solve_square_equation('a', 'b', 'c')


def test__solve_square_equation__params_are_lists():
    with pytest.raises(TypeError):
        solve_square_equation([0], [0], [0])
