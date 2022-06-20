#Заполнить список степенями числа 2
n = int(input("Введите степень числа 2: "))
ch = 2 ** n
print(list(range(2, ch + 1)))

l = []
if n in range(1, n):
    l.append(2**n)
print(l)
