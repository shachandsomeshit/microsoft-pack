import requests
from requests.structures import CaseInsensitiveDict
import tkinter as tk
from tkinter import filedialog
from time import sleep
from os import system
from os import getcwd
from os import chdir

resp = ""


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://api.funcaptcha.com/fc/agf/?pkey=69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC&lang=en',
    'Origin': 'https://api.funcaptcha.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def clear():
    system("cls")

chdir(getcwd())
system("del *mp3")

count = 0
captchas = []


tokens = []
print('tokens:')
while True:
    input_ = input("")
    if input_ == "clear":
        tokens.clear()
        clear();print('tokens:')
        continue
    if input_ == "":
        while "" in tokens:
            tokens.remove("")
        break
    else:
        tokens.append(input_)

for token in tokens:
    data = {
    'token': token,
    'sid': 'eu-west-1',
    'render_type': 'liteJS',
    'lang': 'en',
    'isAudioGame': 'true',
    'analytics_tier': '40',
    'data[status]': 'get_new',
}
    while True:
        resp = requests.post('https://api.funcaptcha.com/fc/gfct/', headers=headers, data=data)
        if "TIMEOUT" in resp.text:
            break
        audio_challenge_urls = resp.json()['audio_challenge_urls']
        for audio in audio_challenge_urls:
            r = requests.get(audio)
            count+=1
            with open('audio' + str(count) + '.mp3', 'wb') as f:
                f.write(r.content)