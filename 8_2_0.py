mylist = [2, 4, 3, 5, 10]
i: int = int(input("Введите элемент списка: "))
t = input("Введите знак > или <: ")
index = mylist.index(i)
for i in mylist:
    if index=="-1" and t==">":
        mylist[-1] = mylist[0]
    elif index=="-1" and t=="<":
        mylist[-1] = mylist[-2]
    elif index!="-1" and index!="0" and t==">":
        mylist[index] = mylist[index+1]
    elif index!="-1" and index!="0" and t=="<":
        mylist[index] = mylist[index-1]
    elif index=="0" and t==">":
        var = mylist[0] = mylist[1]
    else:
        mylist[0] = mylist[-1]
print(mylist[index])

