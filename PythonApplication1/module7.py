import sys
from os import listdir
from os.path import isfile, join

#list all files in directory and version 

def main7():
    files_list = [f for f in listdir('/') if isfile(join('/', f))]
    print("The Version Used")
    print(sys.version)
    print(sys.version_info)

main7()