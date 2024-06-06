"""d"""
from src.operations import sm, minus, mul, pw, divide


def test_sm():
    '''d'''
    assert sm(10,15) == 25
    assert sm(0,0) == 0
    assert sm(12, 24) == 36
    assert sm(0, -1) == -1
    assert sm(-25, 25) == 0

def test_minus():
    '''d'''
    assert minus(15,10) == 5
    assert minus(10,-10) == 20
    assert minus(0,10) == -10
    assert minus(5,10) == -5
    assert minus(0,0) == 0

def test_mul():
    '''d'''
    assert mul(5,5) == 25
    assert mul(2,0) == 0
    assert mul(1,5) == 5
    assert mul(625,10) == 6250
    assert mul(-2,-5) == 10

def test_pw():
    '''d'''
    assert pw(0, 10) == 0
    assert pw(2, 10) == 1024
    assert pw(3, 3) == 27
    assert pw(7, 1) == 7
    assert pw(101, 0) == 1

def test_divide():
    '''d'''
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(1, 2) == 0
    assert divide(15, 4) == 3
    assert divide(-5, -5) == 1

def test_factorial():
    '''d'''
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(7) == 5040
    assert factorial(9) == 362880
