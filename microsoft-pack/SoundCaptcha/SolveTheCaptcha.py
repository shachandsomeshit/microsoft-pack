from os import getcwd, listdir, chdir, system
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from playsound import playsound
import subprocess 
import warnings

chdir(getcwd())

warnings.filterwarnings("ignore")

def cut2three(file):
    subprocess.call("ffmpeg -ss 3 -to 6.3 -i {} audio_ver\\1.wav".format(file), stderr=subprocess.DEVNULL)
    subprocess.call("ffmpeg -ss 7.3 -to 10.6 -i {} audio_ver\\2.wav".format(file), stderr=subprocess.DEVNULL)
    subprocess.call("ffmpeg -ss 11.6 -to 14.9 -i {} audio_ver\\3.wav".format(file), stderr=subprocess.DEVNULL)

def Upload():
    driver1.get("https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/#features")
    driver2.get("https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/#features")
    driver3.get("https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/#features")
    driver1.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[1]/form/div[4]/input").send_keys(getcwd() + "\\" +  "audio_ver\\1.wav")
    driver2.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[1]/form/div[4]/input").send_keys(getcwd() + "\\" +  "audio_ver\\2.wav")
    driver3.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[1]/form/div[4]/input").send_keys(getcwd() + "\\" +  "audio_ver\\3.wav")

def GetTheText():
    while True:
        Text = driver1.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[2]/textarea").text
        Text = Text[93:]
        if "-----------------------" in Text:
            Text = str(Text).replace("-", " ").replace(".", "").replace(",", "").replace("\n", "").replace("\\", " ").replace("/", " ").lower()
            Text = 'Key$@%1000 ' + Text
            list_1 = Text.split(" ")
            break
    while True:
        Text = driver2.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[2]/textarea").text
        Text = Text[93:]
        if "-----------------------" in Text:
            Text = str(Text).replace("-", " ").replace(".", "").replace(",", "").replace("\n", "").replace("\\", " ").replace("/", " ").lower()
            Text = 'Key$@%1000 ' + Text
            list_2 = Text.split(" ")
            break
    while True:
        Text = driver3.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[2]/textarea").text
        Text = Text[93:]
        if "-----------------------" in Text:
            Text = str(Text).replace("-", " ").replace(".", "").replace(",", "").replace("\n", "").replace("\\", " ").replace("/", " ").lower()
            Text = 'Key$@%1000 ' + Text
            list = list_1 + list_2 +  Text.split(" ")
            while '' in list:
                list.remove('')
            return list

def SolveTheSoundCaptcha():
    global list
    TriesCount_ = 0
    TriesCount = 0
    error = 0
    while True:
            options = [i for i, e in enumerate(list) if e == 'Key$@%1000']
            #check if 1 is the key
            if options[1] == 1:
                error +=1
                Key = 1
            #check if 2 is the key
            if options[1]+1 == options[2]:
                error +=1
                Key = 2
            #check if 3 is the key
            try:         
                list[options[2]+1]
            except IndexError:
                error +=1
                Key = 3
            if error > 1:
                if TriesCount == 0:
                        TriesCount +=1
                        system("del audio_ver\\*wav")
                        ChangeFileVolume(file=file,volume=1, output="audio_ver\\audio_.wav" )
                        ChangeFileVolume(file="audio_ver\\bypass.mp3", volume=2, output="audio_ver\\bypass_.wav")
                        CombineAudio(file1="audio_ver\\audio_.wav",file2="audio_ver\\bypass_.wav", output="audio_ver\\audio.wav")
                        cut2three("audio_ver\\audio.wav")
                        Upload()
                        list = GetTheText()
                        continue
                elif TriesCount == 1:
                        TriesCount +=1
                        system("del audio_ver\\*wav")
                        ChangeFileVolume(file=file,volume=2.8, output="audio_ver\\audio_.wav" )
                        ChangeFileVolume(file="audio_ver\\bypass.mp3", volume=1, output="audio_ver\\bypass_.wav")
                        CombineAudio(file1="audio_ver\\audio_.wav",file2="audio_ver\\bypass_.wav", output="audio_ver\\audio.wav")
                        cut2three("audio_ver\\audio.wav")
                        Upload()
                        list = GetTheText()
                        continue
                elif TriesCount == 2:
                        TriesCount +=1
                        system("del audio_ver\\*wav")
                        ChangeFileVolume(file=file,volume=2, output="audio_ver\\audio_.wav" )
                        ChangeFileVolume(file="audio_ver\\bypass.mp3", volume=2, output="audio_ver\\bypass_.wav")
                        CombineAudio(file1="audio_ver\\audio_.wav",file2="audio_ver\\bypass_.wav", output="audio_ver\\audio.wav")
                        cut2three("audio_ver\\audio.wav")
                        Upload()
                        list = GetTheText()
                        continue
            try:
                return Key
            except UnboundLocalError:
                options = [i for i, e in enumerate(list) if e == 'Key$@%1000']
                count = [0,0,0]
                one = list[2:(options[1])]
                two = list[options[1]+2:(options[2])]
                three = list[options[2]+2:(options[2]+2+5000)]
                while 'test' in one:
                    count[0]+=1
                    one.remove('test')
                    continue
                while 'test' in two:
                    count[1]+=1
                    two.remove('test')
                    continue
                while 'test' in three:
                    count[2]+=1
                    three.remove('test')
                    continue
                if one == []:
                    if count[0] > count[1] and count[0] > count[2]:
                        return 1
                else:
                    count[0] = 0
                if two == []:
                    if count[1] > count[0] and count[1] > count[2]:
                        return 2
                else:
                    count[1] = 0
                if three == []:
                    if count[2] > count[0] and count[2] > count[1]:
                        return 3
                else:
                    count[2] = 0
                if TriesCount_ != 2:
                    if TriesCount_ == 0:
                        TriesCount +=1
                        system("del audio_ver\\*wav")
                        ChangeFileVolume(file=file,volume=1, output="audio_ver\\audio_.wav" )
                        ChangeFileVolume(file="audio_ver\\bypass.mp3", volume=1.25, output="audio_ver\\bypass_.wav")
                        CombineAudio(file1="audio_ver\\audio_.wav",file2="audio_ver\\bypass_.wav", output="audio_ver\\audio.wav")
                        cut2three("audio_ver\\audio.wav")
                        Upload()
                        list = GetTheText()             
                        continue
                    else:
                        TriesCount +=1
                        system("del audio_ver\\*wav")
                        ChangeFileVolume(file=file,volume=2.8, output="audio_ver\\audio_.wav" )
                        ChangeFileVolume(file="audio_ver\\bypass.mp3", volume=1, output="audio_ver\\bypass_.wav")
                        CombineAudio(file1="audio_ver\\audio_.wav",file2="audio_ver\\bypass_.wav", output="audio_ver\\audio.wav")
                        cut2three("audio_ver\\audio.wav")
                        Upload()
                        list = GetTheText()     
                        continue
                else:
                    raise Exception("Key Error!")


def ChangeFileVolume(file, volume, output):
   subprocess.call("ffmpeg -i {} -af volume={} -vcodec copy {}".format(file, volume, output), stderr=subprocess.DEVNULL)

def CombineAudio(file1, file2, output):
    subprocess.call("ffmpeg -i {} -i {} -filter_complex amix=inputs=2:duration=longest {}".format(file1,file2, output), stderr=subprocess.DEVNULL)

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
from webdriver_manager.chrome import ChromeDriverManager
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver1 = webdriver.Chrome("chromedriver.exe", chrome_options=options)
driver2 = webdriver.Chrome("chromedriver.exe", chrome_options=options)
driver3 = webdriver.Chrome("chromedriver.exe", chrome_options=options)

AudioFiles = []

files = listdir()
for file in files:
    if ".mp3" in file:
        AudioFiles.append(file)

count=1

for file in AudioFiles:
    print(str(file))
    system("del audio_ver\\*wav")
    ChangeFileVolume(file=file,volume=2.7, output="audio_ver\\audio_.wav" )
    ChangeFileVolume(file="audio_ver\\bypass.mp3", volume=1, output="audio_ver\\bypass_.wav")
    CombineAudio(file1="audio_ver\\audio_.wav",file2="audio_ver\\bypass_.wav", output="audio_ver\\audio.wav")
    cut2three("audio_ver\\audio.wav")
    Upload()
    list = GetTheText()
    Key = str(SolveTheSoundCaptcha())
    print("Key:" + Key)
    count+=1