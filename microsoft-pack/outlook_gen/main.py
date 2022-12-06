from time import sleep
from os import system
from os import popen
import random
from os import path
from pydub import AudioSegment
from os import listdir
from os import getcwd
from sys import getsizeof
from os import stat
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from seleniumwire import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

def SeleniumRetry(seconds, xpath):
    x = 0
    for i in range(seconds):
        try:
            x+=1;driver.find_element_by_xpath(xpath);break
        except NoSuchElementException:
            if x == 20:
                raise NoSuchElementException("Error: Element not found");exit()
        sleep(1)

def CaptchaResearch(tries, timeout):
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
                find_image = network_request.find("https://cdn.funcaptcha.com/fc/assets/graphics/microsoft_identity/Microsoft_Identity_bot_copy.svg")
                if find_image != -1:
                    break
        if find_image != -1:
                break
        if count_tries == tries:
            raise Exception("The captcha wasn't found")

def GetSoundCaptcha(tries ,timeout):
    not_found = 0
    tries_count = 0
    popen("del *mp3").read()
    popen("del *wav").read()
    for i in range(tries):
        tries_count +=1
        sleep(timeout)
        for request in driver.requests:
            if request.response:
                network_request  = (
                    request.url,
                    request.response.status_code,
                    request.response.headers['Content-Type'])
                network_request = str(network_request)
                find_audio_download_link = network_request.find("https://client-api.arkoselabs.com/ags/audio-game-challenges")
                if find_audio_download_link != -1:
                    get_audio_download_link = network_request[find_audio_download_link:(find_audio_download_link+400)].split("'")[0].replace("[", "").replace("'", "")
                    driver.get(get_audio_download_link)
                    break
        if find_audio_download_link != -1:
            break
        if tries_count == tries:
            raise Exception("The captcha was not downloaded")

def Mp3ToWav(tries, timeout):
    tries_count = 0
    for i in range(tries):
        tries_count +=1
        sleep(timeout)
        dir = str(listdir())
        find_audio_file_name = dir.find("audio_verification_challenge")
        find_audio = dir.find(".mp3")
        get_audio_file_name = dir[find_audio_file_name:(find_audio_file_name+440)]
        if find_audio != -1:
            audio_file = get_audio_file_name.split(".")[0] + "." + get_audio_file_name.split(".")[1]+ "." + get_audio_file_name.split(".")[2]  + ".mp3"
            system("rename {0} audio.mp3".format(audio_file))
            break
        if tries_count == tries:
            raise Exception("the process wasn't worked")

def GetSoundCaptchaText(tries, timeout):
    tries_count = 0
    for i in range(tries):
        tries_count +=1
        sleep(timeout)
        page_source = driver.page_source
        find_icon = page_source.find('loader')
        if find_icon == -1:
            for i in range(21):
                actionTab()
            actionEnter()
            sleep(0.25)
            return driver.find_element_by_xpath("/html/body/div[3]/div/div[7]/div/div").text
            break
        if tries_count == tries:
            raise Exception("Error")

def AcceptCookies(tries, timeout):
    tries_count = 0
    for i in range(tries):
        tries_count +=1
        sleep(timeout)
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[1]/div[2]/button[1]").click()
            sleep(1)
            break
        except NoSuchElementException:
            pass
        if tries_count == tries:
            raise Exception("Cookies popup wasn't found")

def ClickOnKeywords():
    actionkeys(Keys.PAGE_DOWN)
    sleep(1)
    for i in range(21):
        actionTab()
    actionEnter()

def SolveTheSoundCaptcha():
    Solution=0
    Error=0
    SoundCaptchaText_ = str(GetSoundCaptchaText(tries=20, timeout=1))
    SoundCaptchaText = SoundCaptchaText_.replace(".", "")
    SoundCaptchaText = SoundCaptchaText.split(" ")
    if SoundCaptchaText[2] == "Option":
        Error+=1
        Solution=1
    elif SoundCaptchaText[2] == "option":
        Error+=1
        Solution=1
    try:
        find_option_2 = SoundCaptchaText.index("2")
    except ValueError:
        find_option_2 = SoundCaptchaText.index("two")
    except ValueError:
        find_option_2 = SoundCaptchaText.index("to")
    except ValueError:
        raise Exception("SpeechRecognitionError")
    if SoundCaptchaText[find_option_2+1] == "Option":
        Error+=1
        Solution=2
    elif SoundCaptchaText[find_option_2+1] == "option":
        Error+=1
        Solution=1
    try:
        find_option_3 = SoundCaptchaText.index("three")
    except ValueError:
        find_option_3 = SoundCaptchaText.index("3")
    except ValueError:
        find_option_3 = SoundCaptchaText.index("tree")
    except ValueError:
        raise Exception("SpeechRecognitionError")
    try:
        SoundCaptchaText[find_option_3+1]
    except IndexError:
        Error+=1
        Solution=3
    if Error > 1:
        pass
    return Solution

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
    months_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
    random_number = random.randint(1,12)
    arrow_amount_months = random_number
    random_month = months_list[random_number-1]
    random_day = random.randint(1,28)
    arrow_amount_days = random_day
    random_year = random.randint(1970, 2000)
    return random_month,random_day, random_year,arrow_amount_days, arrow_amount_months

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

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
prefs = {"download.default_directory" : getcwd()}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

random_username = random_username(length=6)
random_password = random_password(length=10)
name = str(random_username)
name = name.upper()[0] + name[1:-6]
random_last_name = random_last_name()
random_birthday = random_birthday()

print("username:" + random_username)
print("password:" + random_password)
print("name:" + name)
print("last name:" + random_last_name)
print("birthday:" + str(random_birthday[0]) + "/" + str(random_birthday[1]) + "/" + str(random_birthday[2]))


driver.get("https://signup.live.com/signup?")
sleep(0.25)

actionkeys(random_username + "@outlook.com")
actionEnter()

SeleniumRetry(seconds=20, xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[6]/div/div[1]/a[2]")
sleep(0.25)

actionkeys(random_password)
actionEnter()

SeleniumRetry(seconds=20, xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[2]")

actionkeys(name)
actionTab()

actionkeys(random_last_name)
actionEnter()

SeleniumRetry(seconds=20, xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[1]/label")

actionTab()
actionEnter()

for i in range(random_birthday[4]):
    actionArrowDown()
actionEnter()

actionTab()
actionEnter()

for i in range(random_birthday[3]):
    actionArrowDown()
actionEnter()

actionTab()

actionkeys(random_birthday[2])
actionEnter()

CaptchaResearch(tries=20, timeout=1)

print("The captcha was found ✔")

sleep(1)
actionTab()
actionTab()
actionEnter()

GetSoundCaptcha(tries=20, timeout=1)

Mp3ToWav(tries=20, timeout=0.5)

driver.execute_script("window.open('https://speech-to-text-demo.ng.bluemix.net/');")
window_handles = driver.window_handles
sleep(0.25)
driver.switch_to_window(window_handles[1])
SeleniumRetry(seconds=20, xpath="/html/body/div[3]/div/input")

ClickOnKeywords()

sleep(2)

driver.find_element_by_xpath("/html/body/div[3]/div/input").send_keys(getcwd() + "\\audio.mp3")

sleep(2)

AcceptCookies(tries=20, timeout=1)

print(SolveTheSoundCaptcha())

driver.switch_to_window(window_handles[0])

pause()


driver.quit()
exit()