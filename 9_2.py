# Дан двумерный массив 5*5 (список списков). Найти сумму модулей отрицательных нечетных элементов
from random import randint
n: int = 25
a: int = [randint(-10,10) for i in range(n)]
s: int = 0

for i in range(n):
    if a[i]%2==1:
        s=s+a[i]
        s = abs(s)
print([a[i:i + 5] for i in range(0, len(a), 5)])
print("сумма нечетных отрицательных элементов = ",s)
