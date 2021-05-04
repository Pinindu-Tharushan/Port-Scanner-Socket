import os
import socket
Import time
from IPy import IP

os.system("clear")

print('''
╭━━━╮╱╱╱╱╭╮╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
┃╭━╮┃╱╱╱╭╯╰╮╱╱╱┃╭━╮┃\033[0;31mv2.4\033[0;37m╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱\033[0;31m
┃╰━╯┣━━┳┻╮╭╯╱╱╱┃╰━━┳━━┳━━┳━╮╭━╮╭━━┳━╮
┃╭━━┫╭╮┃╭┫┃╱╱╱╱╰━━╮┃╭━┫╭╮┃╭╮┫╭╮┫┃━┫╭╯\033[0;37m
┃┃╱╱┃╰╯┃┃┃╰╮╱╱╱┃╰━╯┃╰━┫╭╮┃┃┃┃┃┃┃┃━┫┃
╰╯╱╱╰━━┻╯╰━╯╱╱╱╰━━━┻━━┻╯╰┻╯╰┻╯╰┻━━┻╯

\033[1;36m =============================================\033[1;m
\033[0;33m|\033[0;32m# Code By Pinindu Tharushan                  \033[0;33m|
\033[0;33m|\033[0;32m  Contact On Whatsapp +94702801713           \033[0;33m|
\033[0;33m|\033[0;32m# Tutorial By Cyber Master                   \033[0;33m|
\033[1;36m =============================================\033[1;m
\033[1;33m|            BEST WEB PORT SCANNER            |
\033[1;36m =============================================\033[00m''')

ipadd = ""
print("[1] Scan With Ip")
print("[2] Scan With Web")
print("[3] Exit")
print()
print("\033[0;32mEnter Your Choose:")

me1 = input("\033[0;36m[~]====>>>> \033[0;37m")

def scan_port(ipadd,port):
    try:
        sock = socket.socket()
        time.sleep(0.5)
        sock.connect((ipadd,int(port)))
        print("\033[0;32m[+] Port " ,int(port), " is Open")
    except:
        print("\033[0;31m[-] Port " ,int(port), " is Closed")

def web(ipadd):
    try:
        print()
        print("\033[0;35mEnter Web Site:")
        web = input()
        ipadd = socket.gethostbyname(web)
    except:
        print()
        print("No Web site Or Typing Error")
        print("Try Again....!")
        exit()

def ip(ipadd):
    try:
        print()
        print("\033[0;35mEnter Web Ip")
        ipadd = input()
    except:
        print()
        print("No IP Or Typing Error")
        print("Try Again....!")
        exit()

if me1 == "1":
    ip(1)
elif me1 == "2":
    web(1)
elif me1 == "3":
    print("Thank You For Using This Tool.....!!!!!")
    print("Exit")
else:
    ip(1)

print()
print("\033[0;34mHow many ports do you want to scan?")
pcount = int(input())

for port in range(0, pcount+1):
    scan_port(ipadd,port)

print("Thank You For Use This Tool")
exit()
