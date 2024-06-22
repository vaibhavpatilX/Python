
def Sub(A,B):
    return A-B

#Decorator
def SmartSub(FPTR):
    def Inner(A,B):
        if(A<B):
            A,B = B,A
        return FPTR(A,B)
    return Inner

def main():
    SubX = SmartSub(Sub)

    Ret = SubX(10,7)
    print("Subtraction is : ",Ret)

    Ret = SubX(7,10)
    print("Subtarction is : ",Ret)
    
if __name__ == "__main__":
    main()