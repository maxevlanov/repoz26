#1. Дан многострочный файл txt
# б) разбить файл на несколько файлов по N строк
N: int = int(input("N: "))

splitLenght: int = N                                # количество строк исходного файла в каждом новом файле
outputBase = "output"                               # новые текстовые документы
input = open("input.txt", "r", encoding="utf-8")    # открываем исходный текстовый файл

count: int = 0
to: int = 1                                         # номер нового файла
dest = None
for line in input:
    if count % splitLenght == 0:
        if dest: dest.close()                       # если ничего не введено, то файл закрывается
        dest = open(outputBase + str(to) + ".txt", "w", encoding="utf-8")   # запись/пересоздание новых файлов
        to += 1                                     # увеличение номера нового файла на 1
    dest.write(line)                                # запись
    count += 1