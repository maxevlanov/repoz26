# 2. Дан многострочный файл, необходимо сформировать новый файл, в котором будет содержатся
# информация по строкам исходного файла (количество слов в каждой строке)
def file_info():
    with open('input.txt', 'r', encoding='utf-8') as file:
        with open('input_info.txt', 'a', encoding='utf-8') as new_file:
            j = 0
            for i in file:
                word_count = len(i.split())
                new_file.write(str(j) + ': ' + str(word_count) + ' words\n')
                j += 1


