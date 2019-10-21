import os
from summarizeDir import *
path = r'C:\Users\tamee\PycharmProjects\directoryInfo\newDir'


if __name__ == '__main__':
     summarizeDirectory(path)
     filenames = os.listdir(path)
     for name in filenames:
         name = f'{path}\\{name}'
         if os.path.isdir(name):
             get_subDir_info(name)