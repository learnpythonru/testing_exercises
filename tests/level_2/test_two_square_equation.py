import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize('coefficients, expected_result', [
    ((1, 0, -4), (-2.0, 2.0)),
    ((1.0, 4, 3.0), (-3.0, -1.0)),
    ((1.0, -4.0, 4.0), (2.0, 2.0)),
    ((1.0, -3.0, 2.0), (1.0, 2.0)),
    ((-2.0, 3.0, -1), (1.0, 0.5)),
])
def test__solve_square_equation__with_two_roots(coefficients, expected_result):
    assert solve_square_equation(*coefficients) == expected_result


@pytest.mark.parametrize('coefficients, expected_result', [
    ((0, -2, 4), (2.0, None)),
    ((0, 2, 6), (-3.0, None)),
    ((0, -2, 2), (1.0, None)),
])
def test__solve_square_eduation__with_one_root(coefficients, expected_result):
    assert solve_square_equation(*coefficients) == expected_result


@pytest.mark.parametrize('coefficients', [
    (0.0, 0.0, 1),
    (1, 2, 5),
    (2.0, 4.0, 2.0000000000001)
])
def test__solve_square_eduation__without_root(coefficients):
    assert solve_square_equation(*coefficients) == (None, None)


@pytest.mark.parametrize('coefficients', [
    (1, 2.0),
    ('1', 2, '3')
])
def test__solve_square_eduation__with_type_error(coefficients):
    with pytest.raises(TypeError):
        solve_square_equation(coefficients)
