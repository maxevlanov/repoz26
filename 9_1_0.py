# Написать программу, которая определяет, является ли список симметричным
lst = [1, 2, 3, 4, 3, 2, 1]

for i in range(len(lst) // 2):
    if lst[i] != lst[-i + 1]:
        print("Список не симметричный")
        break
    else:
        print("Список симметричный")

