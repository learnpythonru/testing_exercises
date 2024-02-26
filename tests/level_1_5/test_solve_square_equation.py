from functions.level_1_5.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
  "square_coefficient, linear_coefficient, const_coefficient, expected_results",
      [
      (0, 0, 0, (None, None)),
      (5, 2, 0, (-0.4, 0.0)),
      (0, 2, 10,(-5.0, None)),
      (0, 2, 0, (0.0, None)),
      (4, 0, -16, (-2.0, 2.0)),
      (5, 3, -26, (-2.6, 2.0)),
      (1, 2, 5, (None, None)),
      (1.1, 2.2, -5.5, (-3.449489742783178, 1.4494897427831779)),
  ]      

)

def test__solve_square_equation__is_valid(square_coefficient, linear_coefficient, const_coefficient, expected_results):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_results


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
