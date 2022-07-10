# Создать квадратную матрицу размером N, на диагонали которой находятся тройки, выше диагонали
# находятся двойки, остальные элементы равны единице
n: int = int(input("Введите размер квадратной матрицы: "))
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 2
        elif i > j:
            a[i][j] = 1
        else:
            a[i][j] = 3
for row in a:
    print(row)
