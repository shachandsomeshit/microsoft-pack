from time import sleep
from os import getcwd, system, listdir, chdir
import warnings
import subprocess
import random
import json
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chdir(getcwd())

warnings.filterwarnings("ignore")

def SeleniumRetry(tries, driver, timeout,  xpath):
    tries_count = 0
    for i in range(tries):
        try:
            driver.find_element_by_xpath(xpath)
            break
        except NoSuchElementException:
            tries_count +=1
            if tries_count == tries:
                raise NoSuchElementException
        sleep(timeout)

def CheckUsername(tries, timeout):
        tries_count = 0
        for i in range(tries):
            tries_count +=1
            for request in driver.requests:
                if request.response:
                    network_request = request.response._body, request.body
                    network_request = str(network_request)
                    FindAvailable = network_request.find("isAvailable")
                    if FindAvailable != -1:
                        return network_request
                        break
            if FindAvailable != -1:
                break
            if tries_count == tries:
                raise Exception("Error")
            sleep(timeout)

def GetExample(tries, timeout):
    for i in range(tries):
        GetExample = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/input").get_attribute("placeholder")
        if GetExample == "New email":
            sleep(timeout)
            continue
        else:
            break

def CaptchaResearch(tries, timeout, search):
    count_tries = 0
    for i in range(tries):
        count_tries +=1
        sleep(timeout)
        for request in driver.requests:
            if request.response:
                network_request  = (
                    request.url,
                    request.response.status_code,
                    request.response.headers['Content-Type'])
                network_request = str(network_request)
                find_image = network_request.find(search)
                if find_image != -1:
                    break
        if find_image != -1:
                break
        if count_tries == tries:
            raise Exception("The captcha wasn't found")

def GetSoundCaptcha(tries ,timeout, search):
    tries_count = 0
    system("del audio\\*mp3")
    for i in range(tries):
        tries_count +=1
        for request in driver.requests:
            if request.response:
                network_request  = (
                    request.url,
                    request.response.status_code,
                    request.response.headers['Content-Type'])
                network_request = str(network_request)
                find_audio_download_link = network_request.find(search)
                if find_audio_download_link != -1:
                    get_audio_download_link = network_request[find_audio_download_link:(find_audio_download_link+400)].split("'")[0].replace("[", "").replace("'", "")
                    driver.get(get_audio_download_link)
                    break
        if find_audio_download_link != -1:
            break
        if tries_count == tries:
            raise Exception("The captcha was not downloaded")
        sleep(timeout)

def DownloadCheck(tries, timeout):
    tries_count = 0
    for i in range(tries):
        tries_count +=1
        sleep(timeout)
        dir = str(listdir("audio\\"))
        find_audio_file_name = dir.find("audio_verification_challenge")
        find_mp3 = dir.find(".mp3")
        find_audio = dir.find("audio")
        get_audio_file_name = dir[find_audio_file_name:(find_audio_file_name+440)]
        if find_mp3 == -1 and find_audio_file_name != -1:
            if settings.method == 1:
                system("rename " + find_audio_file_name + " " +  find_audio_file_name + ".file")
                audio_file = get_audio_file_name.split(".")[0] + "." + get_audio_file_name.split(".")[1]+ "." + get_audio_file_name.split(".")[2] + ".file"
                subprocess.call("ffmpeg -i audio\\{} audio\\audio.wav".format(audio_file), stderr=subprocess.DEVNULL)
                break
        elif find_mp3 != -1 or find_audio != -1:
            if settings.method == 1:
                audio_file = get_audio_file_name.split(".")[0] + "." + get_audio_file_name.split(".")[1]+ "." + get_audio_file_name.split(".")[2]  + ".mp3"
                subprocess.call("ffmpeg -i audio\\{} audio\\audio.wav".format(audio_file), stderr=subprocess.DEVNULL)
            break
        if tries_count == tries:
            raise Exception("the process wasn't worked")

def cut2three(file):
    subprocess.call("ffmpeg -ss 3 -to 6.3 -i {} audio\\1.wav".format(file), stderr=subprocess.DEVNULL)
    subprocess.call("ffmpeg -ss 7.3 -to 10.6 -i {} audio\\2.wav".format(file), stderr=subprocess.DEVNULL)
    subprocess.call("ffmpeg -ss 11.6 -to 14.9 -i {} audio\\3.wav".format(file), stderr=subprocess.DEVNULL)

def Upload():
    driver1.get("https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/#features")
    if settings.method == 1:
        driver2.get("https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/#features")
        driver3.get("https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/#features")
    if settings.method == 2:
        FileName = "audio"
    else:
        FileName = "1"
    driver1.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[1]/form/div[4]/input").send_keys(getcwd() + "\\" +  "audio\\{}.wav".format(FileName))
    if settings.method == 1:
        driver2.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[1]/form/div[4]/input").send_keys(getcwd() + "\\" +  "audio\\2.wav")
        driver3.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[1]/form/div[4]/input").send_keys(getcwd() + "\\" +  "audio\\3.wav")

def GetTheText():
    while True:
        Text = driver1.find_element_by_xpath("/html/body/main/section[2]/div[2]/div/div[1]/div[2]/textarea").text
        Text = Text[93:]
        if "-----------------------" in Text:
            Text = str(Text).replace("-", " ").replace(".", "").replace(",", "").replace("\n", "").replace("\\", " ").replace("/", " ").lower()
            if settings.method == 2:
                return Text
            Text = 'Key$@%1000 ' + Text
            list_1 = Text.split(" ")
            break
    if settings.method == 1:
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
                        system("del audio\\*wav")
                        ChangeFileVolume(file=file,volume=1, output="audio\\audio_.wav" )
                        ChangeFileVolume(file="audio\\bypass.mp3", volume=2, output="audio\\bypass_.wav")
                        CombineAudio(file1="audio\\audio_.wav",file2="audio\\bypass_.wav", output="audio\\audio.wav")
                        cut2three("audio\\audio.wav")
                        Upload()
                        list = GetTheText()
                        continue
                elif TriesCount == 1:
                        TriesCount +=1
                        system("del audio\\*wav")
                        ChangeFileVolume(file=file,volume=2.8, output="audio\\audio_.wav" )
                        ChangeFileVolume(file="audio\\bypass.mp3", volume=1, output="audio\\bypass_.wav")
                        CombineAudio(file1="audio\\audio_.wav",file2="audio\\bypass_.wav", output="audio\\audio.wav")
                        cut2three("audio\\audio.wav")
                        Upload()
                        list = GetTheText()
                        continue
                elif TriesCount == 2:
                        TriesCount +=1
                        system("del audio\\*wav")
                        ChangeFileVolume(file=file,volume=2, output="audio\\audio_.wav" )
                        ChangeFileVolume(file="audio\\bypass.mp3", volume=2, output="audio\\bypass_.wav")
                        CombineAudio(file1="audio\\audio_.wav",file2="audio\\bypass_.wav", output="audio\\audio.wav")
                        cut2three("audio\\audio.wav")
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
                        system("del audio\\*wav")
                        ChangeFileVolume(file=file,volume=1, output="audio\\audio_.wav" )
                        ChangeFileVolume(file="audio\\bypass.mp3", volume=1.25, output="audio\\bypass_.wav")
                        CombineAudio(file1="audio\\audio_.wav",file2="audio\\bypass_.wav", output="audio\\audio.wav")
                        cut2three("audio\\audio.wav")
                        Upload()
                        list = GetTheText()             
                        continue
                    else:
                        TriesCount +=1
                        system("del audio\\*wav")
                        ChangeFileVolume(file=file,volume=2.8, output="audio\\audio_.wav" )
                        ChangeFileVolume(file="audio\\bypass.mp3", volume=1, output="audio\\bypass_.wav")
                        CombineAudio(file1="audio\\audio_.wav",file2="audio\\bypass_.wav", output="audio\\audio.wav")
                        cut2three("audio\\audio.wav")
                        Upload()
                        list = GetTheText()     
                        continue
                else:
                    raise Exception("Key Error!")

def GetAccountMark(tries,timeout):
    for i in range(tries):
        for request in driver.requests:
            if request.response:
                network_request  =(
                    request.url,
                    request.response.status_code,
                    request.response.headers['Content-Type'])
                if str(network_request).find('https://login.live.com/login.srf') != -1:
                    break
        sleep(timeout)
        if i+1 == tries:
            raise Exception("the process wasn't worked")

def random_username(length):
    names_list = requests.get("https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt")
    names_list = names_list.text
    split_names_list  = names_list.split("\n")
    random_name = random.choice(split_names_list)
    random_list = ''.join([str(random.randint(0, 9)) for p in range(0, length)])
    random_username = ''.join([random_name.strip(), random_list.strip() ])
    return random_username

def random_password(length):
    x = str(length/2)
    x = int(x[0])
    length_ = x
    random_letters = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(length_))
    if x == length:
        pass
    else:
        length_ = length-x
    random_numbers = ''.join([str(random.randint(0, 9)) for i in range(0, length_)])
    random_password = ''.join([random_letters.strip(), random_numbers.strip() ])
    return random_password

def random_last_name():
    last_names_list = requests.get("https://raw.githubusercontent.com/arineng/arincli/master/lib/last-names.txt")
    last_names_list = last_names_list.text.lower()
    split_last_names_list = last_names_list.split("\n")
    random_last_name = random.choice(split_last_names_list)
    return random_last_name[0].upper() + random_last_name[1:-1]

def random_birthday():
    random_month = random.randint(1,12)
    random_day = random.randint(1,28)
    random_year = random.randint(1970, 2000)
    return random_month,random_day, random_year

def ChangeFileVolume(file, volume, output):
    subprocess.call("ffmpeg -i {} -af volume={} -vcodec copy {}".format(file, volume, output), stderr=subprocess.DEVNULL)

def CombineAudio(file1, file2, output):
    subprocess.call("ffmpeg -i {} -i {} -filter_complex amix=inputs=2:duration=longest {}".format(file1,file2, output), stderr=subprocess.DEVNULL)

def pause():
    system("pause")

def actionTab():
      actions = ActionChains(driver)
      actions.send_keys(Keys.TAB)
      actions.perform()

def actionArrowDown():
      actions = ActionChains(driver)
      actions.send_keys(Keys.ARROW_DOWN)
      actions.perform()

def actionEnter():
      actions = ActionChains(driver)
      actions.send_keys(Keys.ENTER)
      actions.perform()

def actionSpace():
    actions = ActionChains(driver)
    actions.send_keys(Keys.SPACE)
    actions.perform()

def actionkeys(something):
   actions = ActionChains(driver)
   actions.send_keys(something)
   actions.perform()

def pause():
    system("pause")

f = open('settings.json')
settings_ = json.load(f)

class settings:
    email_pass = settings_["email:pass"]
    email_details = settings_["email details"]
    domain = settings_["domain"]
    mute = settings_["mute"]
    method = settings_['solve method']
    invisible = settings_["invisible"]

if settings.method == 1:
    PublicKey  = "69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC"
elif settings.method == 2:
    PublicKey  = "029EF0D3-41DE-03E1-6971-466539B47725"

from seleniumwire import webdriver

options = webdriver.ChromeOptions()
if settings.invisible == True:
    options.add_argument("--headless")
prefs = {"download.default_directory" : getcwd() + "\\audio"}
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)
driver1 = webdriver.Chrome("chromedriver.exe", chrome_options=options)
if settings.method == 1:
    driver2 = webdriver.Chrome("chromedriver.exe", chrome_options=options)
    driver3 = webdriver.Chrome("chromedriver.exe", chrome_options=options)


for i in range(20):
    _random_username_ = random_username(length=5)
    random_username_ = _random_username_[-1]
    random_username_ =str( _random_username_ + random_username_)
    random_password_ = random_password(length=10)
    name = str(random_username_)
    name = name.upper()[0] + name[1:-6]
    random_last_name_ = random_last_name()
    random_birthday_ = random_birthday()

    if settings.mute == False:
        print("opens the signup page...")

    driver.delete_all_cookies()
    driver.get("https://signup.live.com/signup?")

    actionkeys(random_username_ + "@" + settings.domain)
    actionEnter()

    CheckUsername_ = CheckUsername(tries=20, timeout=1)

    if settings.mute == False:
        print("checks if the email is available...")

    CheckAvailable = str(CheckUsername_).find("isAvailable")
    CheckAvailable = str(CheckUsername_[CheckAvailable:(CheckAvailable+50)]).split(",")[0].replace('isAvailable":', "")
    if CheckAvailable == "false":
        CheckSuggestion = str(CheckUsername_).find("suggestion")
        CheckSuggestion = str(CheckUsername_[CheckSuggestion:(CheckSuggestion+300)])
        CheckSuggestion = CheckSuggestion[15:].split('"')[0]
        driver.refresh()
        GetExample(tries=20, timeout=0.5)
        sleep(1)
        actionkeys(CheckSuggestion)
        actionEnter()
        numbers = []
        for i in CheckSuggestion:
            try:
                numbers.append(int(i))
            except ValueError:
                continue
        last_number = str(numbers).replace(",", "").replace(" ", "").replace("[", "").replace("]", "")[-1]
        random_username_ = CheckSuggestion.split(last_number)[0] + last_number   
        if settings.mute == False:
            print("The email is available")
    else:
        if settings.mute == False:
            print("The email is available")

    with open('emails\\emails.txt') as reader, open('emails\\emails.txt', 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.write("\n")
        writer.truncate()

    if settings.mute == False:
        if settings.email_pass == False:
            print("domain:" + settings.domain)
            print("username:" + random_username_)
            print("password:" + random_password_)
        elif settings.email_pass == True:
            print(str(random_username_ + "@" +  settings.domain) + ":" + random_password_)
        if settings.email_details == True:
            print("name:" + name)
            print("last name:" + random_last_name_)
            print("birthday:" + str(random_birthday_[0]) + "/" + str(random_birthday_[1]) + "/" + str(random_birthday_[2]))

    sleep(1)

    actionkeys(random_password_)
    actionEnter()

    SeleniumRetry(tries=20, driver=driver, timeout=1, xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[2]")

    actionkeys(name)
    actionTab()

    actionkeys(random_last_name_)
    actionEnter()

    SeleniumRetry(tries=20, driver=driver, timeout=1, xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[1]/label")

    actionTab()
    actionEnter()

    for i in range(random_birthday_[0]):
        actionArrowDown()
    actionEnter()

    actionTab()
    actionEnter()

    for i in range(random_birthday_[1]):
        actionArrowDown()
    actionEnter()

    actionTab()

    actionkeys(random_birthday_[2])
    actionEnter()

    CaptchaResearch(tries=20, timeout=1, search='https://client-api.arkoselabs.com/cdn/fc/gc/images/tick.svg')
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/iframe'))
    driver.execute_script('document.getElementById("fc-iframe-wrap").src = "https://client-api.arkoselabs.com/fc/api/nojs/?pkey={}&litejs=1&fb_type=1&session=" + document.getElementById("fc-iframe-wrap").src.split("=")[1].split("&")[0] + "&r=eu-west-1&lang=en"'.format(PublicKey))
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div/div/iframe'))
    if settings.method == 1:
        actionTab()
        actionEnter()
        GetSoundCaptcha(tries=20, timeout=1, search='https://client-api.arkoselabs.com/ags/audio-game-challenges')
        DownloadCheck(tries=20, timeout=0.5)
        system("del audio\\audio.wav")
        system("del audio\\audio_.wav")
        system("del audio\\bypass_.wav")
        file="audio\\audio.wav"
        ChangeFileVolume(file=file,volume=2.7, output="audio\\audio_.wav" )
        ChangeFileVolume(file="audio\\bypass.mp3", volume=1, output="audio\\bypass_.wav")
        CombineAudio(file1="audio\\audio_.wav",file2="audio\\bypass_.wav", output="audio\\audio.wav")
        cut2three("audio\\audio.wav")
        Upload()
        list = GetTheText()
        Key = str(SolveTheSoundCaptcha())
        if int(Key) > 0:
            if settings.mute == False:
                print("The captcha has been solved")
    if settings.method == 2:
        CaptchaResearch(tries=20, timeout=1, search='/standard/fc-litejs.js')
        SeleniumRetry(tries=20, driver=driver, timeout=1, xpath="/html/body/div/div[1]/form/input[5]")
        driver.find_element_by_xpath("/html/body/div/div[1]/form/input[5]").click()
        SeleniumRetry(tries=20, driver=driver, timeout=1, xpath="/html/body/div/div/span/form[2]/button")
        driver.find_element_by_xpath("/html/body/div/div/span/form[2]/button").click()
        SeleniumRetry(tries=20, driver=driver, timeout=1, xpath="/html/body/div/div[1]/a")
        r = requests.get(driver.find_element_by_xpath("/html/body/div/div[1]/a").get_attribute("href"))
        with open("audio\\audio.wav", 'wb') as f:
            f.write(r.content)
        DownloadCheck(tries=20, timeout=0.5)
        Upload()
        Key_ = GetTheText()
        Key = ""
        for i in Key_:
            try:
                int(i)
                Key += i
            except (ValueError):
                continue
        print(Key)

    sleep(3)
    if settings.email_pass == True:
        emails_file = open("emails\\emails.txt", "a")
        emails_file.write(random_username_ + "@" +  settings.domain + ":" + random_password_)
        emails_file.close()

    elif settings.email_pass == False:
        emails_file = open("emails\\emails.txt", "a")
        emails_file.write("\ndomain:" +  settings.domain + "\nusername:" + random_username_ + "\npassword:" + random_password_)
        emails_file.close()

    if settings.email_details == True:
        emails_file = open("emails\\emails.txt", "a")
        emails_file.write("\nname:" + name + "\nlast name:" + random_last_name_ + "\nbirthday:" + str(random_birthday_[0]) + "/" + str(random_birthday_[1]) + "/" + str(random_birthday_[2]))
        emails_file.close()

    sleep(3)
    driver.refresh()