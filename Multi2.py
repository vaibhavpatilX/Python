import multiprocessing
import os

def Task1(Value):
    print("Executing the first task...")
    print("PID of running process for Task1 is : ",os.getpid())

def Task2(Value):
    print("Executing the Second Task...")
    print("PID of running process for Task2 is : ",os.getpid())

def main():
    print("Demonstration of Multiprocssing")
    print("PID of running process is : ",os.getpid())

    No = 5
    p1 = multiprocessing.Process(target = Task1, args = (No,))
    p2 = multiprocessing.Process(target = Task2, args = (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()