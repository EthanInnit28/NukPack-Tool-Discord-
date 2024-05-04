from Config.Util import *
from Config.Config import *
import requests

Title("Discord Token Joiner")

token = input(f"{color.BLUE}\n{INPUT} Token -> {color.RESET}")
invite = input(f"{color.BLUE}{INPUT} Server Invitation -> {color.RESET}")

invite_code = invite.split("/")[-1]

try:
    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
    if response.status_code == 200:
        server_name = response.json().get('guild', {}).get('name')
    else:
        server_name = invite
except:
    server_name = invite

try:
        headers = {
            'Authorization': token
        }
        response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers)
        
        if response.status_code == 200:
            print(f"\n{blue}[{white}{current_time_hour()}{blue}] {ADD} Status: {color.WHITE}Joined{color.BLUE} | Server: {color.WHITE}{server_name}{color.BLUE}\n")
        else:
            print(f"\n{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Error {response.status_code}{color.BLUE} | Server: {color.WHITE}{server_name}{color.BLUE}\n")
except:
    print(f"\n{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Error{color.BLUE} | Server: {color.WHITE}{server_name}{color.BLUE}\n")

Continue()
Reset()