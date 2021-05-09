import calculator as calc


def test_when_input_none():
    # input
    a = None
    b = 3
    op = "-"
    # process
    result = calc.calculate(a, b, op)
    # assertion
    assert result is None
