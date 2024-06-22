
def Add(A,B):
    return A+B

#Function accepts parameter as another function
def Marvellous(FPTR):
    print(type(FPTR))
    print(FPTR)
    Ans = FPTR(11,7)
    print("Addition is : ",Ans)

def main():
    Arr = Marvellous(Add)

if __name__ == "__main__":
    main()  