#1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
N: int = int(input("N: "))                          # на сколько файлов будем разбивать исходный
with open("input.txt", "r", encoding="utf-8") as file:  # открытие исходного файла
    lines = file.readlines()                   # считываем из файла все строки в виде списка и возвращаем его

end = 0
for i in range(1, N+1):
    if i == 1:
        start = 0
    increase = int(len(lines) / N)                  # увеличиваем
    end = end + increase
    with open("input" + str(i) + ".txt", "w") as file:  # открываем полученные файлы
        for line in lines[start:end]:
            file.write(line)
    start = end