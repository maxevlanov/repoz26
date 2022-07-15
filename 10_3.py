# 3. Дан файл с многострочным текстом, необходимо развернуть содержимое файла и содержимое каждой строки
with open('for10_3.txt', 'r', encoding='utf-8') as file:
    lines = [line[::-1].strip() for line in file]
    lines.reverse()
with open('for10_3.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(lines))
