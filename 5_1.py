N = int(input("Введите число N: "))
M = int(input("Введите число М: "))
K = int(input("Введите число К: "))
ch = 0
for i in range(N):
    if ch % M == 0 and ch > K:
        print(ch)
    ch += 1
