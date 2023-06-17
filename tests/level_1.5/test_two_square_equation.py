from functions.level_1_5.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
    'square_coefficient, linear_coefficient, const_coefficient, expected_result',
    [
        (2.12, 4.5, 8.55, (None, None)),
        (1, 3, 2, (-2.0, -1.0)),
        (0, 2, 2, (-1.0, None)),
        (0, 0, 2, (None, None)),
    ],
)
def test__salve_square_equation(square_coefficient, linear_coefficient, const_coefficient, expected_result):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_result
