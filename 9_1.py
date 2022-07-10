# Написать функцию, которая определяет, является ли список симметричным
s = input()


def palindrome():
    snew = s.replace(" ", "").lower()
    ls = len(snew)
    if snew[:ls // 2] == snew[ls // 2 + 1:][::-1]:
        return "Палиндром"
    return "Не палиндром"
