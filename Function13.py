
#Function define another function inside it and return as its return value
def Demo():
    def Add(A,B):
        return A+B

    return Add

def main():
    Ret = Demo()
    Ans = Ret(10,7)
    print("Addition is : ",Ans)
    
if __name__ == "__main__":
    main()  