import os
from tkinter import filedialog
from tkinter import *


try:
    f = open("Data/saves.txt",  mode ="r", encoding = "ibm039")
    f.close()
except:
    try:
        os.makedirs("Data")
        mycmd = 'attrib +s +h "Data"'
        os.system(mycmd)
    except FileExistsError:
        pass
    f = open("Data/saves.txt",  mode ="w", encoding = "ibm039")
    f.close()


F = open("Data/saves.txt",  mode ="a", encoding = "ibm039")
x = 0

def Read(line=False, x = None, all = False, FileName = "Data/saves.txt"):
    F = open(FileName,  mode ="r", encoding = "ibm039")
    if line == False:
        y = F.read(x)
        return y
    if line == True:
        content = F.readlines()
        content = [i.strip() for i in content]
        if not(all):
            y = content[x-1]
        else:
            y = content[x-1:]
        return y
    F.close()

    



def clear(): return os.system('cls')



z = Read(x=1)
if not(z):
    Pass = input("Enter New Password: ")
    F = open("Data\saves.txt", mode ="a", encoding = "ibm039")
    print(Pass, file = F)
    print("show", file = F)
    F.close()
    folder = filedialog.askdirectory()
    print("Directory to hide: ",end="")
    print(folder)
    input()
    F = open("Data\saves.txt", mode ="a", encoding = "ibm039")
    print(folder, file = F)
    f.close()
clear()


PassTry = input("Enter Password: ")
if PassTry == str(Read(line = True, x = 1)):
    clear()
    folder = str(Read(line=True,x=3))
    if Read(line=True,x=2) == "show":
        mycmd = 'attrib +s +h "' + folder +'"'
        os.system(mycmd)
        password = Read(line = True,x=1)
        F = open("Data\saves.txt", mode ="w", encoding = "ibm039")
        print(password, file = F)
        print("hide", file = F)
        print(folder, file = F)
        F.close()
    elif Read(line=True,x=2) == "hide":
        mycmd = 'attrib -s -h "' + folder +'"'
        os.system(mycmd)
        password = Read(line = True,x=1)
        F = open("Data\saves.txt", mode ="w", encoding = "ibm039")
        print(password, file = F)
        print("show", file = F)
        print(folder, file = F)
        F.close()
    In = str(input("You want to restart?(y/n) "))
    if In == "y":
        folder = str(Read(line=True,x=3))
        mycmd = 'attrib -s -h "' + folder +'"'
        os.system(mycmd)
        os.remove("Data/saves.txt")
        os.rmdir("Data")
