import os
from os import walk
path = r'C:\Users\tamee\PycharmProjects\directoryInfo\newDir'

def summarizeDirectory(p):
    with open("dirInfo.txt","a")as fp:
        fp.write(f"directory name : {os.path.splitext(p)[0]}\n")
        fp.write(f"directory size : {os.path.getsize(p)}\n")
        fp.write((f'num of file : {get_num_of_file(p)}\n'))
        numOfSub = get_num_of_subDir(p)
        fp.write((f'num of sub directory : {numOfSub}\n'))
        if numOfSub != 0 :
            fp.write((f'sub directory info :\n'))


def get_subDir_info(p):
    summarizeDirectory(p)

def get_num_of_file(path):
    count = 0
    for name in  os.listdir(path):
        name = f'{path}\\{name}'
        if os.path.isfile(name):
            count+=1
    return count

def get_num_of_subDir(path):
    count = 0
    for name in  os.listdir(path):
        name = f'{path}\\{name}'
        if os.path.isdir(name):
            count+=1
    return count



if __name__ == '__main__':

    summarizeDirectory(path)
    for name in os.listdir(path):
        name = f'{path}\\{name}'
        if os.path.isdir(name):
            get_subDir_info(name)