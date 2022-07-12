# 2. Дан многострочный файл, необходимо сформировать новый файл, в котором будет содержатся
# информация по строкам исходного файла (количество слов в каждой строке)
f_handlers = {}
with open("input.txt", "r", encoding="utf-8") as inp_file:

    for line in inp_file:
        w_len = len(line.strip())
        if w_len == 0:                              # исключаем слова с нулевой длиной
            continue
        fn = f'words_{w_len}.txt'
        f = f_handlers.setdefault(fn, open(fn, 'w+'))
        f.write(line)

for handler in f_handlers.values():
    handler.close()


