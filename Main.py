import socket
from IPy import IP
import os


try:
	system.os("clear")
except:
	system.os("cls")
except:
	print()

print('''
╭━━━╮╱╱╱╱╭╮╱╭━━━╮
┃╭━╮┃╱╱╱╭╯╰╮┃╭━╮┃\033[0;31mv1.0
┃╰━╯┣━━┳┻╮╭╯┃╰━━┳━━┳━━┳━╮╭━╮╭━━┳━╮
┃╭━━┫╭╮┃╭┫┃╱╰━━╮┃╭━┫╭╮┃╭╮┫╭╮┫┃━┫╭╯
\033[0;37m┃┃╱╱┃╰╯┃┃┃╰╮┃╰━╯┃╰━┫╭╮┃┃┃┃┃┃┃┃━┫┃
╰╯╱╱╰━━┻╯╰━╯╰━━━┻━━┻╯╰┻╯╰┻╯╰┻━━┻╯

\033[1;36m =============================================\033[1;m
\033[0;33m|\033[0;32m# Code By Pinindu Tharushan                  \033[0;33m|
\033[0;33m|\033[0;32m  Contact On Whatsapp +94702801713           \033[0;33m|
\033[0;33m|\033[0;32m# Tutorial By Cyber Master                   \033[0;33m|
\033[0;33m|\033[0;32m# Tutorial By xOR                            \033[0;33m|
\033[0;33m|\033[0;32m# Tutorial Black hat                         \033[0;33m|
\033[1;36m =============================================\033[1;m
\033[1;33m|            BEST WEB PORT SCANNER            |
\033[1;36m =============================================\033[00m''')

try:
    print("[1] Scan With Web")
    print("[2] Scan With IP")
    print("[3] Exit Tool")
    print()
    print("\033[0;32m[~] Enter Your choose ")
    menu = input("\033[0;36m[~]=======>> \033[0;37m")

    def main(ipaddress):
        def scan_port(ipaddress,port):
            try:
                sock = socket.socket()
                sock.settimeout(0.5)
                sock.connect((ipaddress, port))
                print("\033[0;32m[+] Port " + str(port) + " is Open")
            except:
                print("\033[0;31m[-] Port " + str(port) + " is Closed")

        print()
        count = int(input("Enter How Many Ports Do You Want Scan: "))
        for port in range(1, int(count)+1):
            scan_port(ipaddress,port)

    def web():
        print()
        web = input("Enter Web: ")
        ipaddress = socket.gethostbyname(web)
        print("This Web IP is " + ipaddress)
        main(ipaddress)

    def ip():
        print()
        ipaddress = input("Enter Web: ")
        print("Your IP Is " + ipaddress)
        main(ipaddress)

    try:
        if menu == 1:
            web()
        elif menu == 2:
            ip()
        elif menu == 3:
            print()
            print("Thank You For Use This Tool..!")
            exit()
        else:
            web()
    except:
        print()
        print("Typing Error")

except InterruptedError:
    print()
    print("Stoped By User")
    print("Thank You For Use this tool...")

except:
    print()
    print("Script Error...!")
    print("contact us.")