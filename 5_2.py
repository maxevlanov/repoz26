while True:
    print("Для завершения работы с калькултором введите Py")
    ch1: int = int(input("Введите число 1: "))
    oper: str = input("Введите знак  операции: ")
    if oper not in ("+", "-", "*", "**", "/"):           #проверка введенной операции
        continue
    if oper == "Py":         #завершение работы с калькулятором
        break
    ch2: int = int(input("Введите число 2: "))
    if oper == "+":
        print(ch1 + ch2)
    elif oper == "-":
        print(ch1 - ch2)
    elif oper == "*":
        print(ch1 * ch2)
    elif oper == "**":                   #возведение в степень
        print(ch1 ** ch2)
    elif oper == "/" and ch2 != 0:
        print(ch1 / ch2)
    else:
        print("На ноль делить нельзя!")