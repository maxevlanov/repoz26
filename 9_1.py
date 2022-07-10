# Написать функцию, которая определяет, является ли список симметричным
a = [1,2,3,3,2,1]


def is_symmetric(string):
    if len(a) == 1:
        return True
    else:
        return a[0] == my_str[-1] and is_symmetric(a[1:-1])