#!/usr/bin/python3
# -*- coding: UTF-8
# 2021 Info Gathering

import time
import os
import sys
import requests
import json

#########
#colores#
#########

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def consulta_telefonica():
   os.system("clear")
   time.sleep(1)
   print(""" 
  
    \033[33m▄███████▄    ▄█    █▄     ▄██████▄  ███▄▄▄▄      ▄████████       \033[31m▄█        ▄██████▄   ▄██████▄     ▄█   ▄█▄ ███    █▄     ▄███████▄ 
    \033[33m███    ███   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███     \033[31m ███       ███    ███ ███    ███   ███ ▄███▀ ███    ███   ███    ███ 
    \033[33m███    ███   ███    ███   ███    ███ ███   ███   ███    █▀       \033[31m███       ███    ███ ███    ███   ███▐██▀   ███    ███   ███    ███ 
    \033[33m███    ███  ▄███▄▄▄▄███▄▄ ███    ███ ███   ███  ▄███▄▄▄          \033[31m███       ███    ███ ███    ███  ▄█████▀    ███    ███   ███    ███ 
  \033[33m▀█████████▀  ▀▀███▀▀▀▀███▀  ███    ███ ███   ███ ▀▀███▀▀▀          \033[31m███       ███    ███ ███    ███ ▀▀█████▄    ███    ███ ▀█████████▀  
   \033[33m ███          ███    ███   ███    ███ ███   ███   ███    █▄       \033[31m███       ███    ███ ███    ███   ███▐██▄   ███    ███   ███        
    \033[33m███          ███    ███   ███    ███ ███   ███   ███    ███      \033[31m███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ ███    ███   ███        
   \033[33m▄████▀        ███    █▀     ▀██████▀   ▀█   █▀    ██████████      \033[31m█████▄▄██  ▀██████▀   ▀██████▀    ███   ▀█▀ ████████▀   ▄████▀
   
 \033[37mCode by \033[33mBlackCage
   """)

   api_key = 'f1494a44d7eab4aa220832a4b04f4fc2'
   number = input('Introduzca el número de teléfono:\033[32m ')
   print("")
   time.sleep(1)
   # Petición

   data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

   for key, value in data.json().items():

      print("%s: %s" % (key, value))

   print("")

def verificador_email():
   os.system("clear")
   time.sleep(1)
   print(""" 
  
     \033[33m▄████████   ▄▄▄▄███▄▄▄▄      ▄████████  ▄█   ▄█             \033[31m▄█    █▄     ▄████████  ▄█        ▄█  ████████▄     ▄████████     ███      ▄██████▄     ▄████████ 
    \033[33m███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███  ███            \033[31m███    ███   ███    ███ ███       ███  ███   ▀███   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
    \033[33m███    █▀  ███   ███   ███   ███    ███ ███▌ ███            \033[31m███    ███   ███    ███ ███       ███▌ ███    ███   ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
   \033[33m▄███▄▄▄     ███   ███   ███   ███    ███ ███▌ ███            \033[31m███    ███   ███    ███ ███       ███▌ ███    ███   ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
  \033[33m▀▀███▀▀▀     ███   ███   ███ ▀███████████ ███▌ ███            \033[31m███    ███ ▀███████████ ███       ███▌ ███    ███ ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   
    \033[33m███    █▄  ███   ███   ███   ███    ███ ███  ███            \033[31m███    ███   ███    ███ ███       ███  ███    ███   ███    ███     ███     ███    ███ ▀███████████ 
    \033[33m███    ███ ███   ███   ███   ███    ███ ███  ███▌    ▄      \033[31m███    ███   ███    ███ ███▌    ▄ ███  ███   ▄███   ███    ███     ███     ███    ███   ███    ███ 
    \033[33m██████████  ▀█   ███   █▀    ███    █▀  █▀   █████▄▄██      \033[31m ▀██████▀    ███    █▀  █████▄▄██ █▀   ████████▀    ███    █▀     ▄████▀    ▀██████▀    ███    ███ 
                                                                                                                                                      ███    ███ 


 \033[37mCode by \033[33mBlackCage
   """)

   api_key = 'd7aee7d2ea5a44d05a83027a1bc764dd'
   correo = input('Introduzca la dirección de correo:\033[32m ')
   print("")
   time.sleep(1)
   # Petición

   data = requests.get("http://apilayer.net/api/check?access_key=%s&email=%s&smtp=1&format=1" % (api_key, correo))

   for key, value in data.json().items():

      print("%s: %s" % (key, value))

   print("")

def iplookup():
   os.system("clear")
   time.sleep(1)
   print("""
  
     
\033[33m ██▓ ██▓███    \033[31m  ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
\033[33m▓██▒▓██░  ██▒   \033[31m▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
\033[33m▒██▒▓██░ ██▓▒   \033[31m▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
\033[33m░██░▒██▄█▓▒ ▒   \033[31m▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
\033[33m░██░▒██▒ ░  ░   \033[31m░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
\033[33m░▓  ▒▓▒░ ░  ░   \033[31m░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
\033[33m ▒ ░░▒ ░        \033[31m░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
\033[33m ▒ ░░░          \033[31m  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
\033[33m ░              \033[31m    ░  ░    ░ ░      ░ ░  ░  ░      ░              
                                                                  

 \033[37mCode by \033[33mBlackCage
   """)

   api_key = '8e5c2cfcdcf8b3686e71c0c4a32ca4c5'
   ip = input('Introduzca la dirección IP:\033[32m ')
   print("")
   time.sleep(1)
   # Petición

   data = requests.get("http://api.ipstack.com/%s?access_key=%s&format=1" % (ip, api_key))

   for key, value in data.json().items():

      print("%s: %s" % (key, value))

   print("")


# banner
def portada():
    os.system("clear")
    time.sleep(1)
    print("""
    \033[33m██████╗░███████╗██████╗░░██████╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░
    \033[33m██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░░░
    \033[33m██████╔╝█████╗░░██████╔╝╚█████╗░██║░░██║██╔██╗██║███████║██║░░░░░
    \033[33m██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║██║╚████║██╔══██║██║░░░░░
    \033[33m██║░░░░░███████╗██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░░██║███████╗
    \033[33m╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝
    \033[31m██╗░░██╗██╗████████╗
    \033[31m██║░██╔╝██║╚══██╔══╝
    \033[31m█████═╝░██║░░░██║░░░
    \033[31m██╔═██╗░██║░░░██║░░░
    \033[31m██║░╚██╗██║░░░██║░░░
    \033[31m╚═╝░░╚═╝╚═╝░░░╚═╝░░░
    \033[36m                                               
    \033[37mCode by :\033[33m BlackCage\033[36m
    
        pnlookup         \033[33m[ Phone Number LookUp ]\033[36m
        
        iplookup         \033[33m[ IP Adress LookUp ]\033[36m

        ealookup         \033[33m[ Email Adress LookUp ]\033[36m
        
        eavalidator      \033[33m[ Email Adress Validator ]\033[36m
        
        slowloris        \033[33m[ Open SlowLoris Script ]\033[36m
        
        help 		 \033[33m[ Show This Pannel ]
""")
def opciones():
    opcion = input("\033[33mBlack@\033[33mCage:\033[39m ")
    if opcion == "pnlookup":
       consulta_telefonica()
       opciones()
       
    if opcion == "iplookup":
       iplookup()
       opciones()

    if opcion == "ealookup":
        time.sleep(1)
        os.system("clear && cd modules && bash email.sh")
        
    if opcion == "eavalidator":
       verificador_email()
       opciones()
        
    if opcion == "slowloris":
        os.system("clear")
        time.sleep(1)
        print("""
  \033[31m░██████╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗
  \033[31m██╔════╝██║░░░░░██╔══██╗░██║░░██╗░░██║
  \033[31m╚█████╗░██║░░░░░██║░░██║░╚██╗████╗██╔╝
  \033[31m░╚═══██╗██║░░░░░██║░░██║░░████╔═████║░
  \033[31m██████╔╝███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░
  \033[31m╚═════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░
  \033[36m██╗░░░░░░█████╗░██████╗░██╗░██████╗
  \033[36m██║░░░░░██╔══██╗██╔══██╗██║██╔════╝
  \033[36m██║░░░░░██║░░██║██████╔╝██║╚█████╗░
  \033[36m██║░░░░░██║░░██║██╔══██╗██║░╚═══██╗
  \033[36m███████╗╚█████╔╝██║░░██║██║██████╔╝
  \033[36m╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝╚═════╝░
        """)
        time.sleep(1)
        print("\033[32mEjemplo: www.ejemplo.com")
        web = input("\033[32mIntroduzca la página web:\033[36m ")
        os.system("clear && cd modules && perl slowloris.pl -dns " + web)
	
    if opcion == "help":
        time.sleep(1)
        os.system("clear")
        portada()
        opciones()
      
    else:
        print("""\033[31m
    
        Invalid option, please, try again.
        """)
        time.sleep(1.5)
        os.system("clear")
        portada()
        opciones()

portada()
opciones()
