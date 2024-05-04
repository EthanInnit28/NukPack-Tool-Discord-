from Config.Util import *
from Config.Config import *
from selenium import webdriver

Title("Discord Token Login")

token = input(f"{color.BLUE}\n{INPUT} Token -> {color.RESET}")

print(f"""
{color.WHITE}[{color.BLUE}01{color.WHITE}] {color.BLUE}->{color.WHITE} Chrome
{color.WHITE}[{color.BLUE}02{color.WHITE}] {color.BLUE}->{color.WHITE} Firefox
{color.WHITE}[{color.BLUE}03{color.WHITE}] {color.BLUE}->{color.WHITE} Edge
""")
choice = input(f"{color.BLUE}{INPUT} Browser -> {color.RESET}")

try:
    if choice == '1':
        navigator = "Chrome"
        print(f"{color.BLUE}{INFO} {navigator} Starting..{color.RESET}")
        driver = webdriver.Chrome()
        print(f"{color.BLUE}{INFO} {navigator} Ready !{color.RESET}")

    elif choice == '2':
        navigator = "Firefox"
        print(f"{color.BLUE}{INFO} {navigator} Starting..{color.RESET}")
        driver = webdriver.Firefox()
        print(f"{color.BLUE}{INFO} {navigator} Ready !{color.RESET}")

    elif choice == '3':
        navigator = "Edge"
        print(f"{color.BLUE}{INFO} {navigator} Starting..{color.RESET}")
        driver = webdriver.Edge()
        print(f"{color.BLUE}{INFO} {navigator} Ready !{color.RESET}")

    else:
        ErrorChoice()
    
    script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
    driver.get("https://discord.com/login")
    print(f"{color.BLUE}{INFO} Token Connection..")
    driver.execute_script(script + f'\nlogin("{token}")')
    time.sleep(4)
    print(f"{color.BLUE}{INFO} Connected Token !")
    print(f"{color.YELLOW}{INFO} If you leave the tool, edge will close!")
    input(f"{color.BLUE}{INPUT} Leave Edge (enter) -> {color.WHITE}")
    Reset()
except:
    print(f"{color.BLUE}{ERROR} {navigator} not installed or driver not up to date.")
    Continue()
    Reset()