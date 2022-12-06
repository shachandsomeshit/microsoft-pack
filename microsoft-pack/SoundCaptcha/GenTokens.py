import requests
from requests.structures import CaseInsensitiveDict
import tkinter as tk
from tkinter import filedialog
from os import system

tokens = ""

system("cls")

print("""
███████╗██╗░░░██╗███╗░░██╗░█████╗░░█████╗░██████╗░████████╗░█████╗░██╗░░██╗░█████╗░
██╔════╝██║░░░██║████╗░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░██║██╔══██╗
█████╗░░██║░░░██║██╔██╗██║██║░░╚═╝███████║██████╔╝░░░██║░░░██║░░╚═╝███████║███████║
██╔══╝░░██║░░░██║██║╚████║██║░░██╗██╔══██║██╔═══╝░░░░██║░░░██║░░██╗██╔══██║██╔══██║
██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝██║░░██║██║░░░░░░░░██║░░░╚█████╔╝██║░░██║██║░░██║
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗░██████╗
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║██╔════╝
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║╚█████╗░
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║░╚═══██╗
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
""")



tokens_amount = input("How much tokens do you want ?")
PublicKey = input("public key:") 


data = {
    'public_key': PublicKey,
    'lang': 'en',
    'language': 'en',
    'render_type': 'liteJS',
    'fallback_type': '0',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://api.funcaptcha.com/fc/agf/?pkey={}&lang=en'.format(PublicKey),
    'Origin': 'https://api.funcaptcha.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

captchas = []

tokens_amount = int(tokens_amount)

for i in range(tokens_amount):
    resp = requests.post('https://api.funcaptcha.com/fc/gt/nojs/' + PublicKey, headers=headers, data=data)
    token = str(resp.json()['token']).split("|")[0]
    tokens+=token + "\n"
    captchas.append("https://client-api.arkoselabs.com/fc/gc/?token={}&r=eu-west-1&metabgclr=%23ffffff&maintxtclr=%231B1B1B&mainbgclr=%23ffffff&guitextcolor=%23747474&metaiconclr=%23757575&meta_height=325&meta=7&lang=en&pk={}&at=1&ag=101&cdn_url=https%3A%2F%2Fclient-api.arkoselabs.com%2Fcdn%2Ffc&lurl=https%3A%2F%2Faudio-eu-west-1.arkoselabs.com&surl=https%3A%2F%2Fclient-api.arkoselabs.com&smurl=https%3A%2F%2Fclient-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager".format(token, PublicKey))
    print(token)
print("Do you want to save the tokens in a file? (y/N)")
SaveAnswer = input("").lower()
if SaveAnswer == "y":
    save = filedialog.asksaveasfile(mode="w", title="Save To A File", filetypes =[('Text Files', '*.txt')], defaultextension='.txt')
    open(save.name, "w").write(tokens.strip())
elif SaveAnswer == "n":
    pass
else:
    print("You can type only (y/N)")
    exit()
print("Do you want to get the captchas ? (y/N)")
CaptchasAnswer = input("").lower()
if CaptchasAnswer == "y":
    print("links:")
    for captcha in captchas:
        print(captcha)

