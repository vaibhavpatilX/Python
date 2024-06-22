
from sys import *
import os
import hashlib

def hashlib(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hasglib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

        print("Error : Invalid number of arguments")
        exit()

        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to traverse specific directory")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : ApplicationName AbsoluePAth_Of_Directory")
            exit()

        try :
            DirectoryWatcher(argv[1])
        
        except ValueError:
            print("Error : Invalid datatype of input")
        
        except Exception :
            print("Error : Invalid input")

"""if __name__ == "__main__":
    main()"""
        print(path)
        print(file_hash)
        print('')
    else : 
        print("Invalid Path") 

def main():
    print("----Application by Vaibhav Patil----")

    print("Application Name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1]== "*H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extension")
        exit()
    try:
        arr = DisplayChecksum(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input",E)
        
if __name__ == "__main__":
    main()
