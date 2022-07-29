import os

path = "C:\\Users\\User\\PycharmProjects\\repoz26\endpoints\\v1"

def obhodFile(path, level=1):
    print("Level=",level, os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+"\\"+i):
            print("Down:", path+"\\"+i)
            obhodFile(path+"\\"+i, level+1)
            print("Return in:", path)
obhodFile(path)