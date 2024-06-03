from src.operations import * 

def test_sum():
  assert sum(10,15) == 25

def test_minus():
  assert minus(15,10) == 5

def test_mul():
  assert mul(5,5) == 25

def test_pow():
  assert pow(0, 10) == 0

def test_divide():
  assert divide(10, 2) == 5
