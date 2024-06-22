def CheckEven(Value):
    
    Result = Value % 2
    
    if(Result == 0):
        print("No is Even")
    else:
        print("No is Odd")
    


def main():
    No = 0
    
    print("Enter number : ")
    No = int(input())
    
    CheckEven(No)
      
if __name__ == "__main__":
    main()