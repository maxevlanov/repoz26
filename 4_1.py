"""Заполнить список степенями числа 2"""
n = int(input("Введите степень числа 2: "))
chisla: int = [2**i for i in range(1, n+1)]
print(chisla)