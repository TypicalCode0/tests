from src.operations import * 

@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    [
        (10, 3, 13),
        (-1, 5, 4),
        (0, 0, 0),
    ],
)
def test_sum(a, b, result):
  assert sum(a,b)==result

@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    [
        (10, 3, 7),
        (-1, 5, -6),
        (0, 0, 0),
    ],
)
def test_minus(a, b, result):
  assert minus(a,b)==result

@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    [
        (10, 3, 30),
        (-1, 5, -5),
        (0, 0, 0),
    ],
)
def test_mul(a, b, result):
  assert mul(a,b) == result

@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    [
        (10, 3, 1000),
        (1, 0, 1),
        (3, 2, 9),
    ],
)
def test_pow(a, b, result):
  assert pow(a, b) == result

@pytest.mark.parametrize(
    ('a', 'b', 'result'),
    [
        (6, 3, 2.0),
        (-1, 5, -0.2),
        (0, 5, 0.0),
    ],
)
def test_divide(a, b, result):
  assert divide(a, b) == result
