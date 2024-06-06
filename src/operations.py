"""lol"""


def sm(a: int, b: int) -> int:
    '''a + b'''
    return a + b

def mul(a: int, b: int) -> int:
    '''a * b'''
    return a * b

def minus(a: int, b: int) -> int:
    '''a - n'''
    return a - b

def pw(a: int, b: int) -> int:
    '''a**b'''
    return a**b

def divide(a: int, b: int) -> int:
    '''a / b'''
    return a // b

def factorial(a: int) -> int:
    '''a!'''
    res = 1
    for i in range(2, a + 1):
        res *= 2
    return res
