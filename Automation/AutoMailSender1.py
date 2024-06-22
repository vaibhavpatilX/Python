import os
import time
import psutil
import urllib.request  # Corrected import
import smtplib
import schedule
from sys import argv
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# ...
def is_connected():
    try:
        response = urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        print("URL Error:", err)
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False


def MailSender(filename, timestamp):
    try:
        fromaddr = "vaibhavpatilvp8016@gmail.com"
        toaddr = "patil.vaibhax@gmail.com"
        password = "kamal@2508"  # Use your App Password or Gmail account password

        msg = MIMEMultipart() 

        msg['From'] = fromaddr
        msg['To'] = toaddr

        # ... (rest of your email composition code)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, password)

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log file successfully sent through mail")
    except Exception as E:
        print("Unable to send mail:", E)

# Make sure to replace "your_app_password_here" with your actual App Password or Gmail account password.

def ProcessLog(log_dir='Vaibhav'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    timestamp = time.ctime()
    # Replace spaces and other invalid characters with underscores
    sanitized_timestamp = ''.join(c if c.isalnum() or c in ('-', '_') else '_' for c in timestamp)
    log_path = os.path.join(log_dir, "MarvellousLog%s.log" % sanitized_timestamp)
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("My File Process Logger : " + timestamp + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % log_path)

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path, timestamp)
        endTime = time.time()

        print('Took %s seconds to send mail' % (endTime - startTime))
    else:
        print("There is no internet connection")

def main():
    print("---- My File by Vaibhav Patil----")

    print("Application name : " + argv[0])

    if len(argv) != 2:
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used log record of running processes")
        exit()
        
    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage: ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")
    
    except Exception as E:
        print("Error : Invalid input", E)

if __name__ == "__main__":
    main()
