from functions.level_1_5.two_square_equation import solve_square_equation


def test__solve_square_equation__normal_input():

    square_coefficient = 2
    linear_coefficient = 2
    const_coefficient = - 12

    square_equation = solve_square_equation(
        square_coefficient,
        linear_coefficient,
        const_coefficient
        )

    assert square_equation == (-3.0, 2.0)


def test__solve_square_equation__discriminant_below_zero():

    square_coefficient = 1
    linear_coefficient = 1
    const_coefficient = 1

    square_equation = solve_square_equation(
        square_coefficient,
        linear_coefficient,
        const_coefficient
        )

    assert square_equation == (None, None)


def test__solve_square_equation__discriminant_is_zero():

    square_coefficient = 1
    linear_coefficient = 2
    const_coefficient = 1

    square_equation = solve_square_equation(
        square_coefficient,
        linear_coefficient,
        const_coefficient
        )

    assert square_equation == (-1.0, -1.0)


def test__solve_square_equation__discriminant_is_zero():

    square_coefficient = 1
    linear_coefficient = 2
    const_coefficient = 1

    square_equation = solve_square_equation(
        square_coefficient,
        linear_coefficient,
        const_coefficient
        )

    assert square_equation == (-1.0, -1.0)


def test__solve_square_equation__a_is_zero_b_is_zero():

    square_coefficient = 0
    linear_coefficient = 0
    const_coefficient = 1

    square_equation = solve_square_equation(
        square_coefficient,
        linear_coefficient,
        const_coefficient
        )

    assert square_equation == (None, None)


def test__solve_square_equation__a_is_zero():

    square_coefficient = 0
    linear_coefficient = -2
    const_coefficient = 2

    square_equation = solve_square_equation(
        square_coefficient,
        linear_coefficient,
        const_coefficient
        )

    assert square_equation == (1, None)
