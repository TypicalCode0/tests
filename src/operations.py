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


while True:
    print("Введите команду. Доступные команды:")
    print("exit - выход из программы\nenter - ввод мат. выражения")
    cmd = input()
    if cmd == "exit":
        break
    elif cmd == "enter":
        s = input("Введите выражение через пробел -> ").split()
        print("Результат: ", sep="", end="")
        if s[1] == "+":
            print(sm(int(s[0]), int(s[2])))
        elif s[1] == "-":
            print(minus(int(s[0]), int(s[2])))
        elif s[1] == "*":
            print(mul(int(s[0]), int(s[2])))
        elif s[1] == "/":
            print(divide(int(s[0]), int(s[2])))
        elif s[1] == "**":
            print(pw(int(s[0]), int(s[2])))
