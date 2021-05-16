import calculator as calc
import pytest


def test_when_input_none():
    # input
    a = None
    b = 3
    op = "-"
    # process
    result = calc.calculate(a, b, op)
    # assertion
    assert result is None


def test_division_by_zero():
    # input
    a = 1
    b = 0
    operator = "/"

    # process and assert
    with pytest.raises(ZeroDivisionError):
        result = calc.calculate(a, b, operator)


def test_multiply_success():
    # input
    a = 2
    b = 5
    operator = "*"

    # process
    result = calc.calculate(a, b, operator)

    assert result == 10


def test_sum_success():
    a = 2
    b = 2
    operator = "+"

    result = calc.calculate(a, b, operator)

    assert result == 4


def test_subtract_success():
    a = 5
    b = 2
    operator = "-"

    result = calc.calculate(a, b, operator)

    assert result == 3


def test_invalid_operator():
    a = 10
    b = 20
    operator = "9"

    # process
    result = calc.calculate(a, b, operator)

    assert result == "No valid operator!"