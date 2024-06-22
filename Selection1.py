
def main():
    No = 0
    
    print("Enter number : ")
    No = int(input())
    
    Result = No % 2
    
    if(Result == 0):
        print("No is Even")
    else:
        print("No is Odd")
    
if __name__ == "__main__":
    main()