"""d"""
from src.operations import sm, minus, mul, pw, divide


def test_sm():
    '''d'''
    assert sm(10,15) == 25

def test_minus():
    '''d'''
    assert minus(15,10) == 5

def test_mul():
    '''d'''
    assert mul(5,5) == 25

def test_pw():
    '''d'''
    assert pw(0, 10) == 0

def test_divide():
    '''d'''
    assert divide(10, 2) == 5
