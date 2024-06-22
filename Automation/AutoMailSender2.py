from sys import *
import schedule
import time
import os
import psutil
import urllib3
# C:\Users\Gauri\AppData\Local\Programs\Python\Python37\Lib\site-packages\psutil\__init__.py
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


def is_connected():
    try:
        urllib3.connectionpool.connection_from_url('http://216.58.192.142 ', timeout=1)
        # urllib3.connection_from_url('https://www.google.com/ ',timeout=1)   #https://www.google.com/   #http://216.58.192.142
        return True
    except urllib3.URLError as err:
        return False


def MailSender(filname, time):
    try:
        fromaddr = "vaibhavpatilvp8016@gmail.com"
        toaddr = "patil.vaibhavx@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
                Hello %s,
                       Welcome to XYZ company.
                       Please find attached document which contains Log of Running Process.
                       Log file is created at : %s

                       This is auto generated mail.

                Thanks and Regards,
                Vaibhav Patil
                """ % (toaddr, time)

        subject = """Process log generted at : %s""" % time

        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filname, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename=%s" % filname)

        msg.attach(p)
        # print("LLLLLL")
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()
        #print("JJJJJJj")
        s.login(fromaddr, "qeer zser milm fjwm")
        #print("KKKKKKK")
        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log file successfully sent throught Mail")

        print("hhhhh")
    except Exception as E:
        print("Unable to send mail", E)


def ProcessLog(log_dir="Vaibhav"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass  # is same as continue

    separator = "-" * 80
    log_path = os.path.join(log_dir, " file %s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Process Logger:""\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % (log_path))

    connected = is_connected()

    if connected:
        starttime = time.time()
        MailSender(log_path, time.ctime())
        endtime = time.time()

        print('Took %s seconds to send mail' % (endtime - starttime))


def main():
    print("Process Monitoring Automation with periodic Mail Sender....")
    print("Application name:" + argv[0])

    if (len(argv) != 2):
        print("Invalid number of argumnets")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used log record of running processess")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minute.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input", E)


if __name__ == "__main__":
    main()