string = [2,5,7,9,10]
x = input("введите интересующий вас элемент из списка: ")
while x not in string:

    x = input("введите интересующий вас элемент из списка: ")
    t = input("введите знак > или <: ")
    a = 0
    for i in range(string):
        if t == ">":
            string[i] == string[i+1]
            a+=1
        else:
            string[i] == string[i-1]
print(string)
