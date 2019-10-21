import os
from summarizeDir import *
path = r'C:\Users\tamee\PycharmProjects\directoryInfo\newDir'


if __name__ == '__main__':
    try:
        summarizeDirectory(path)
    except ValueError as ex:
        print(ex.args)
        summarizeDirectory(r'C:\Users\tamee\PycharmProjects\directoryInfo')
