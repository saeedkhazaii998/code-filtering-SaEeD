import os
import sys
import datetime
import pyfiglet
from colorama import Fore
from time import sleep

os.system("clear")
os.system("pip install colorama")
os.system("pip install datetime")
os.system("pip install pyfiglet")
os.system("clear")



print(Fore.RED+pyfiglet.figlet_format("SaEeD"))

bnr = (Fore.RED+f""""
--> Hellow
----> Im SaEeD
-----> Welcome to my script


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠤⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⢀⣀⣀⠀⠠⠤⢀⡑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠅⠒⠈⠉⠀⠀⠀⠀⢀⡀⠀⠘⡀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢠⣤⣄⡀⠀⢀⣴⡾⠛⠛⠓⠀⢱⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠉⣩⠻⠖⡘⠛⣴⣶⣦⣤⠴⢄⣧⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⠾⠿⠿⠀⣾⡀⠉⠉⠁⠀⠀⠀⣿⠺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⢿⠇⢠⠠⠤⢠⡤⠂⢸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡠⣖⣁⣻⣶⣾⣥⣤⣴⣿⡏⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡻⡛⣉⣻⣿⡭⠄⢀⠞⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣌⠀⠈⣿⡇⠀⠈⡠⠪⠏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠙⢷⡤⠻⠇⠤⠊⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⡔⠁⢠⠀⠀⠙⠢⣀⠀⠀⠀⠀⣠⠇⢳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡀⠤⠀⠒⠊⠉⠀⠀⡇⠀⠘⡄⠀⠀⠀⠈⠑⢢⡤⢼⡁⠀⢸⠀⠉⢶⠠⢀⡀⠀⠀⠀⠀⠀
⡎⠁⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⢻⢦⠀⠀⠀⡴⠋⠀⠀⠙⡄⢸⡆⠀⠈⡄⠀⠈⠉⠐⠢⡄⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠠⠃⠀⠀⠈⡄⠑⣄⡞⢆⠀⠀⢀⠜⠙⠊⢱⠀⠀⠘⡄⠀⠀⠀⠀⠘⡄
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠄⠀⠀⣧⠀⠈⠀⢰⠋⠁⠘⣄⠀⠀⠸⡄⠀⠠⠃⠀⠀⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠐⠀⠂⠒⠐⠒⠀⠀⠂⠒⠒⠒⠒⠐⠂⠒⠀⠒⠂⠀⠀⠀
       """)
for i in bnr:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.009)

x = str(datetime.datetime.now())
print()
print()

print(Fore.GREEN+"START TIME ----> " + (x))

print()
print()
sleep(0.9)

code = input(Fore.YELLOW+""""
(1) ----> Bug 
(2) ----> Bug numbers           
(3) ----> Bug linux
(4) ----> Bug server 
(5) ----> Bug spam          
(6) ----> Algoritm
(7) ----> Virus
(8) ----> link Virus
(9) ----> Ds
(10) ----> Video sexy 
(11) ----> picture sexy
(12) ----> Site porn
(13) ----> Site zeb rhbr
(14) ----> Site shitan prasti 
(15) ----> Site Gun
(16) ----> Site Terrorist 
(17) ----> Site Fishing 
(18) ----> Site Dark Web
(19) ----> Site Hack rubika 
(20) ----> Site mozer
(21) ----> Mokharab
(22) ----> Mokharab Ip
(23) ----> Mokharab Fishing 
(24) ----> Mokharab linux 
(25) ----> Mokharab Fata
(26) ----> Jlb knnde 
(27) ----> hasas be server 
Please Enter The Number ==> : """)
print("")
print(Fore.CYAN+F"-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-")
print("")

if code == "1":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"(15.0.9.0.2-1).1.3.8.0.6.0.0.0.1.1.5.4.3.7.-8.5/0/3.pornhub.com) %s' % (fg('red'), bg('yellow'), attr('reset')))")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "2":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://2.1.4.9/e////f.h/1.3.0.2.8.1.4.7.1.8.2.7.2.7.9.1.2.8.3.1.9.7.2.1.8.4.6.8.4.1.8.1.5.7.1.3.6")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "3":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://linux.io/killd-0000.4-spam%100/bug-3.5.4-linux")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "4":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://Server.onilline.oflline.bg/rubika+5.106.8.151/bug-on.of-server")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "5":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://Spam.rubika.ir/Spam%100/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7(Spam_Account)...spam%100/=(target=❗️)=/yftt15k/-Spam_100.k                                 ❗️=id target")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "6":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://Support.bot/1.3.5.4/gk//DarkWeb-000-tor//15k/8.1.2.8.4.9.2.9.1.4.1.0.1.73.1.3.4.2.0.6.3.9.1.5.3.3.3.1.0.1.0.3.Kmni.4.3.5.1.3.1.0.7.2.4.6.3.5.1.0.1.0.3.4.3.4//违反规则//3.4.2.0.6.3.9.1.5.3/-Cyberpolice.gov.ir")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "7":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"R0B1KA</bug_Bug_bUg/>11.11.Viru3.12.12/page.viruses/-V-infec")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "8":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://ffmodmenu.page.link/LatestMODMENU")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "9":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://dxprit-hack-yftt15k-filter-supportbot-fil.phpnet.us/x.photo.html")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "10":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://uploadkon.ir/uploads/358504_23VID-20231104-144658-787.mp4")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "11":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://uploadkon.ir/uploads/4ddf16_23InShot-۲۰۲۳۰۴۱۷-۰۲۴۷۲۲۳۴۸.jpg | https://s8.uupload.ir/files/crdghzedz1lx_6ew0.jpg")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "12":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://m.me11r.com")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "13":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://www.al-monitor.com/originals/2023/03/iran-death-khamenei-chants-nowruz-leader-gives-victorious-speech")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "14":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://www.hailsatanfilm.com")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "15":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://www.gunsinternational.com")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "16":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://www.dni.gov/nctc/ftos/isis_fto.html")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "17":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://wiki.aa419.org/index.php/Main_Page")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "18":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://darkweblive.net")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "19":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://hamyargps.com/blog/remote-rubika-hack")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "20":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://freedomhacker.net/top-free-websites-to-learn-hacking-2016-4842")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "21":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://185.172.128.8/ma.exe")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "22":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://www.blocklist.de/lists/courierpop3.txt")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "23":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://dibbs.ai.arizona.edu/dibbs/azsecure-phishingwebsites-3/output_20257-21113.tar")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "24":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "25":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"https://cyberpolice.gov.ir/node/168853")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "26":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"http://web.rubika.ir/#c=b0Y0a2cafbaf668e282d2dc02a1fe2a7")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")

if code == "27":
    sleep(0.3)
    print(Fore.BLUE+"loding")
    sleep(1)
    sleep(0.9)
    print("")
    print("")
    print(Fore.YELLOW+"(Server.onlline/server.offline.onlline/)")
    sleep(0.9)
    print("")
    print("")
    print(Fore.LIGHTMAGENTA_EX+"God Bye")
