
class Demo:
    def __init__(self,Value1,Value2):
        print("Inside init method")
        self.No1 = Value1
        self.No2 = Value2

    def Display(self):
        print("Value of No1 : ",self.No1)
        print("Value of No : ",self.No2)

def main():
    print("Demonnstration of Object Orientation")

    obj1 = Demo(10,20)
    obj2 = Demo(11,21)

    obj1.Display()
    obj2.Display()

if __name__ == "__main__":
    main()