import sum


def test_sum(a, b):
  assert sum(a,b)==a+b

def test_minus(a, b):
  assert minus(a,b)==a-b

def test_mul(a, b):
  assert mul(a,b) == a*b

def test_pow(a, b):
  assert pow(a, b) == a**b

def test_divide(a, b):
  assert divide(a, b) == a / b
