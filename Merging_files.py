import os
import shutil
file1 = input("Enter the name of file1: ")
file2 = input("Enter the name of file2: ")
Destination = input("Enter the destination filename: ")
with open(Destination,"wb") as wfd:
    for files in(file1,file2):
        with open(files,"rb")as fd:
            shutil.copyfileobj(fd,wfd)
check = open(Destination,"r")
print(check.read())
check.close()