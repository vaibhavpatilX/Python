import datetime
import schedule
import time

def Schedule_Minute():
    print("Schedule schedules after a minute...")
    print("Current time is : ",datetime.datetime.now())

def Schedule_Hour():
    print("Schedule schedules after a hour...")
    print("Current time is : ",datetime.datetime.now())

def Schedule_Sunday():
    print("Schedule schedules after each Sunday...")
    print("Current time is : ",datetime.datetime.now())

def main():
    print("Automation using Python..!")

    schedule.every(1).minute.do(Schedule_Minute)
    schedule.every().hour.do(Schedule_Hour)
    schedule.every().Sunday.do(Schedule_Sunday)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()