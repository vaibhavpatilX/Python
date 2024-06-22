import os

def main():
    print("Enter the name of file that you want to open for reading purpose : ")
    File_name = input()

    if os.path.exists(File_name):
        fobj = open(File_name,"r")
        if fobj:
            print("File successfully opened in the read mode..!")

            Line1 = fobj.readline()
            Line2 = fobj.readline()
            Line3 = fobj.readline()

            print("Data from file is  :")
            for line in fobj:
                print(line)
        
        else:
            print("Unable to open file..!")
    else:
        print("There is no such file..!")
    

if __name__ == "__main__":
    main()