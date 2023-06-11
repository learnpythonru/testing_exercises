from functions.level_1_5.two_square_equation import solve_square_equation
import pytest

@pytest.mark.parametrize(
        "square_coefficient,linear_coefficient,const_coefficient,expected_result",
        [
            (1, 2, -3, (-3.0, 1.0)),
            (1, 1, 1, (None, None)),
            (0, 0, 1, (None, None)),
            (0, -2, 2, (1.0, None)),
            pytest.param(
                         1, 2, 1, (-1.0, None),
                         marks=pytest.mark.xfail(reason='should be one root for dicriminant is zero')),
        ],
        ids=[
            'normal_input',
            'discriminant_below_zero',
            'a_is_zero_b_is_zero',
            'a_is_zero',
            'discriminant_is_zero'
        ]
)
def test__solve_square_equation__successfull(square_coefficient,
                                             linear_coefficient,
                                             const_coefficient,
                                             expected_result,
                                             ):
    assert solve_square_equation(
                                square_coefficient,
                                linear_coefficient,
                                const_coefficient,
                                ) == expected_result
