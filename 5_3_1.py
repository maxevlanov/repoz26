N: int = int(input("Введите число N: "))
z: int = 5          #количество чисел в строке
i: int = 2
while i <= N:
    if i != 0 and i % 2 == 0:
        if i % 10 == 0:
            print(i, end="\n")
        else:
            print(i, end=" ")
    i += 1
