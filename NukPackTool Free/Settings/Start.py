# Discord: fhttps://discord.gg/nukpacksq
# Coded / Dev / Owner: Ethan
# Copyright © NukPackSQ
######################################################### 


from Program.Config.Config import *
from Program.Config.Util import *
from colorama import init, Fore
import requests
import re
import webbrowser

Clear()
Title("Menu")
popup_version = ""

# Testo verde chiaro
green_light = Fore.LIGHTGREEN_EX

# Testo verde scuro
green_dark = Fore.GREEN

option_01 = "Discord-Webhook-Spammer"
option_02 = "Discord-Token-Nuker"
option_03 = "Discord-Token-Joiner"
option_04 = "Discord-Token-Leaver"
option_05 = "Discord-Token-Login"

option_01_txt = color.WHITE + option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = color.WHITE + option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = color.WHITE + option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = color.WHITE + option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = color.WHITE + option_05.ljust(30)[:30].replace("-", " ")

page1 = f"""{white}[{cyan}DISCORD{white}]

   {white}[{red}01{white}] {lightblack_ex}-{white} {option_01_txt}
   {white}[{red}02{white}] {lightblack_ex}-{white} {option_02_txt}
   {white}[{red}03{white}] {lightblack_ex}-{white} {option_03_txt}
   {white}[{red}04{white}] {lightblack_ex}-{white} {option_04_txt}
   {white}[{red}05{white}] {lightblack_ex}-{white} {option_05_txt}"""

while True:
   try:
      with open("Settings/Program/Config/Page.txt", "r") as file:
         page = file.read()
      if page in ["1"]:
         page = page1
         Title("Pagina 1")
      else:
         page = page1
         Title("Page 1")
   except:
      page = page1
      Title("Page 1")
   Clear()
   print(f"""{popup_version}{blue}                                                                                                                       
{lightblack_ex}              ...                            
{lightblack_ex}             ;::::;                           
{lightblack_ex}           ;::::; :;                          
{lightblack_ex}         ;:::::'   :;                         
{lightblack_ex}        ;:::::;     ;.         
{lightblack_ex}       ,:::::'       ;          {white} OOO\        {red}╔═══════════{lightred_ex}═════════════════════════════{white}════════════╗
{lightblack_ex}       ::::::;       ;          {white}OOOOO\       {red}║    {white}Created BY {cyan}Ethan                                {white}║
{lightblack_ex}       ;:::::;       ;         {white}OOOOOOOO      {red}║    {white}This tool was created {cyan}ONLY {white}for discord! {white}        ║  
{lightblack_ex}      ,;::::::;     ;'         {white}/ OOOOOOO     {red}╚══════════{lightred_ex}═══════════{white}═══════════════════════════════╝
{lightblack_ex}    ;:::::::::`. ,,,;.        {white}/  / DOOOOOO         
{lightblack_ex}  .';:::::::::::::::::;,     {white}/  /     DOOOO        
{lightblack_ex} ,::::::;::::::;;;;::::;,   {white}/  /        DO{lightred_ex}OO       
{lightblack_ex};`::::::`'::::::;;;::::: ,#{white}/  {lightred_ex}/          {lightred_ex}DOOO      
{lightblack_ex}:`:::::::`;::::::;;::: ;::#  {lightred_ex}/            {lightred_ex}DOOO     
{lightblack_ex}::`:::::::`;:::::::: ;::::# {red}/              {lightred_ex}D{red}OO     
{lightblack_ex}`:`:::::::`;:::::: ;::::::#{red}/               {red}DOO     
{lightblack_ex} :::`:::::::`;; ;::::::::{lightred_ex}:##                {red}OO     
{lightblack_ex} ::::`:::::::`;:::::::{lightred_ex}:;:{red}::#                {red}OO
{lightblack_ex} `:::::`::::::::::::;'`:{red};::#           {red}×    {red}O      
{lightblack_ex}  `:::::`::::::::;' {white}/  / {red}`:#                 {red}× 
{lightblack_ex}   ::::::`:::::;'  {white}/  /   {red}`#              {red}×

   {page}
""")
   choice = input(f"""{cyan}┌───({white}{username_pc}-> [Free]{cyan})
{cyan}└──{cyan}> {reset}""")

   if choice in ['1', '01']:
      StartProgram(f"{option_01}.py")

   elif choice in ['2', '02']:
      StartProgram(f"{option_02}.py")

   elif choice in ['3', '03']:
      StartProgram(f"{option_03}.py")

   elif choice in ['4', '04']:
      StartProgram(f"{option_04}.py")

   elif choice in ['5', '05']:
      StartProgram(f"{option_05}.py")

   else:
      ErrorChoiceStart()