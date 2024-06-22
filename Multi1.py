import multiprocessing
import os

def Task1():
    print("Executing the first task...")
    print("PID of running process for Task1 is : ",os.getpid())

def Task2():
    print("Executing the Second Task...")
    print("PID of running process for Task2 is : ",os.getpid())

def main():
    print("Demonstration of Multiprocssing")

    print("PID of running process is : ",os.getpid())

    Task1()
    Task2()

if __name__ == "__main__":
    main()