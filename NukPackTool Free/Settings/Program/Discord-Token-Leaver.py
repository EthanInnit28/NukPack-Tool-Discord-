from Config.Util import *
from Config.Config import *
import requests
import threading

Title("Discord Token Leaver")

token = input(f"{color.BLUE}\n{INPUT} Token -> {color.RESET}")
r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
if r.status_code == 200:
    pass
else:
    ErrorToken()

def LeaveServer(guilds, token):
    for guild in guilds:
        try:
            response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
            if response.status_code == 204 or response.status_code == 200:
                print(f"{green}[{white}{current_time_hour()}{green}] {ADD} Status: {color.WHITE}Leave{color.GREEN} | Server: {color.WHITE}{guild['name']}")
            elif response.status_code == 400:
                requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
                print(f"{green}[{white}{current_time_hour()}{green}] {ADD} Status: {color.WHITE}Leave{color.GREEN} | Server: {color.WHITE}{guild['name']}")
            else:
                print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Error{color.BLUE} | Server: {color.WHITE}{guild['name']}")
        except Exception as e:
            print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Error: {e}{color.BLUE}")

if token.startswith("mfa."):
    print(f"{blue}[{white}{current_time_hour()}{blue}] {ERROR} Status: {color.WHITE}Error: Mfa enabled{color.BLUE}")

processes = []
guilds_id = requests.get("https://discord.com/api/v8/users/@me/guilds", headers={'Authorization': token}).json()
if not guilds_id:
    print(f"{INFO} No Server found.")
    Continue()
    Reset()
for guild in [guilds_id[i:i+3] for i in range(0, len(guilds_id), 3)]:
    t = threading.Thread(target=LeaveServer, args=(guild, token))
    t.start()
    processes.append(t)
for process in processes:
    process.join()
Continue()
Reset()