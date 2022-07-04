D: int = int(input("Введите глубину: "))
P = []
for i in range(D):
    row = [1]*(i+1)     #дублирование 1 слева
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)
for r in P:
    print(r)