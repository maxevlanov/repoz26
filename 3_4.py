#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
ch1 = input("Введите число 1: ")
ch2 = input("Введите число 2: ")
ch3 = input("Введите число 3: ")
ch4 = ch1 + ch2 + ch3
print("Количество отрицательных чисел: ")
print(ch4.count("-"))
print("Количество положительных чисел: ")
print(3 - ch4.count("-"))