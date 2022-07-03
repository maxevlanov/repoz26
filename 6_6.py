def main(l):
	a = list( i for i in l if l.index(i) % 2 == 0) + list(i for i in l if l.index(i) % 2 != 0)
	return a
lst = input("Введите числа: ").split()
print(*main(lst))
