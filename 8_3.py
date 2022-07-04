a: str = "affakfgggffffghjjj21333"
b: str = "afklkfgggffkfhjjjj12"


def str_match_2(a,b):
    num = 0
    for i in range(min(len(a), len(b))):
        if a[i : i+1] == b[i : i+1]:
            num += 1
    return num


print(str_match_2(a,b))