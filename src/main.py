"""asd"""
from src.operations import sm, pw, mul, minus, divide


while True:
    print("Введите команду. Доступные команды:")
    print("exit - выход из программы\nenter - ввод мат. выражения")
    cmd = input()
    if cmd == "exit":
        break
    if cmd == "enter":
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
        elif s[1] == "!":
            print(factorial(int(s[0])))
