"""Заполнить словарь где ключами будут выступать числа от 0 до n, а значениями вложенный словарь с ключами "name" и "email", а значения
для этих ключей будут браться с клавиатуры"""
n: int = int(input("Введите количество ключей: "))
my_dict2: dict = {}
my_dict1: dict = {}
for i in range(1, n + 1):
    my_dict1[i] = "name"
    name = str(input("Введите имя: "))
for j in range(1, n + 1):
    my_dict2[j] = "email"
    email = str(input("Введите адрес электронной почты: "))
print(my_dict1)
print(my_dict2)
