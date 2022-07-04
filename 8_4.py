List_Max = [3, 15, 10, 0, -2, 5, 6]
a: int = 1
while a < len(List_Max):
    for i in range(len(List_Max) - a):
        if List_Max[i] > List_Max[i + 1]:
            List_Max[i], List_Max[i + 1] = List_Max[i + 1], List_Max[i]
    a += 1
print(List_Max)
