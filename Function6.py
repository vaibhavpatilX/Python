
#Function accepts multiple parameter and return multiple
def Marvellous(Value1, Value2):
    Addition = Value1 + Value2
    Subtraction = Value1 - Value2
    Multiplication = Value1 * Value2

    return Addition,Subtraction,Multiplication

def main():
    Ret = Marvellous(11,6)
    print(type(Ret))
    print("Addition is : ",Ret[0])
    print("Subtraction is : ",Ret[1])
    print("Multiplication is : ",Ret[2])
    
if __name__ == "__main__":
    main()  