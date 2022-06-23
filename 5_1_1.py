N = int(input("Введите число N: "))
M = int(input("Введите число М: "))
K = int(input("Введите число К: "))
i = j = 0
while i != N:
    if j % M == 0 and j > K:
        print(j)
    i += 1
    j += 1