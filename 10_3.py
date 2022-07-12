# 3. Дан файл с многострочным текстом, необходимо развернуть содержимое файла и содержимое каждой строки
file = open("input.txt", "r", encoding="utf-8")
s = file.readlines()
file[s::-1]
s.reverse()
print(''.join(s).strip('\n'))
