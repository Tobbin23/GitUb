#!/usr/bin/python3
"""
autor Tobbin23
"""
from requests import get
from requests.auth import HTTPBasicAuth
import json
import os
import sys
import subprocess
import re
from src.barvy import Barvy
from spravce import cesta
from src.autor import logo_b, logo_a
from src.user_agent import user

"""
Vytrorit script pro jednodusi stahovani programu z github.
misto manualniho otevirani stranek a klikani na copy reposit.
Vyzada si uzivatelske jmeno a reposit daneho autora a programu.
nasledne ho potvrdi a stahne pomoci git clone <url>.
"""

class Mo:

    nazev_slozky = ""
    
    # 
    def se_t(jmeno):
        try:
            adresa = get(f"https://api.github.com/users/{jmeno}/starred?page=1&per_page=100",headers=user())
            if adresa.status_code == 200:
                print("\tSpojení %s %d " % (Barvy.OK, adresa.status_code))
                
                load = adresa.json()
                for i in range(0, len(load)):
                    i + 1
                    with open("scraping.json", mode="w", encoding="utf-8") as zapis:
                        json.dump(load, zapis, indent=True)
                    sys.stdout.flush()
                       
            else:
                print(f"\t{Barvy.FAIL}{Barvy.BOLD}Uživatel nebyl nalezen{Barvy.RESET}\n"\
                      f"\t{Barvy.FAIL}{Barvy.BOLD}Zkontroluj te, prosím připojeni k internetu{Barvy.RESET}")
                
    
        except ConnectionAbortedError as f:
            print(f)
        except ValueError:
            print("chybí hodnota")

        
    def ret(a):

        with open("scraping.json", mode="r", encoding="utf-8") as prohledni:
            data = prohledni.read()
            dec = json.loads(data)                
            prohledni.close()
        if a:
            
            for i in range(0, len(dec)):
                if a in dec[i]:
                    print("\n")
                
                    print(f"\t{Barvy.BOLD}\t",dec[i][a],flush=True)
                else:
                    pass
        elif not a:
            for i in range(0, len(dec)):
                print("\t====\n")
                
                print(f"\t{Barvy.BOLD}Project number: ", i+1,f"{Barvy.RESET}")
                print(f"\t{Barvy.BOLD}Reposit name: ",dec[i]["name"],f"{Barvy.RESET}")
                print(f"\t{Barvy.BOLD}\tLogin: ", dec[i]["owner"]["login"],f"{Barvy.RESET}")
                print(f"\t{Barvy.BOLD}\tDescription: ",dec[i]["description"],f"{Barvy.RESET}")
                print(f"\t{Barvy.BOLD}\tUrl: ", dec[i]["html_url"],f"{Barvy.RESET}")
                print(f"\t{Barvy.BOLD}\tClone:",dec[i]["clone_url"],f"{Barvy.RESET}")
                print(f"\t{Barvy.BOLD}\tLanguage: ", dec[i]["language"],f"{Barvy.RESET}")
                print(f"\t{Barvy.BOLD}\tReposit size: ",dec[i]["size"]/1024,"Mb",f"{Barvy.RESET}") 
            prohledni.close
        else:
            pass
        sys.stdout.flush()
        
        
            
    def clon():
        with open("scraping.json", mode="r", encoding="utf-8") as stahni:    
            data = stahni.read()
            dec = json.loads(data)
            Login = dec[0]["owner"]["login"]
            pocet = len(dec[0]["owner"]["login"])
            if pocet > len(Mo.nazev_slozky) and Login != Mo.nazev_slozky:
                del Mo.nazev_slozky
                Mo.nazev_slozky = Login
                print(f"{Barvy.BOLD}Jmeno složky> {Barvy.slozka}{Mo.nazev_slozky}{Barvy.RESET}",flush=True)
            else:
                del Mo.nazev_slozky
                Mo.nazev_slozky = Login                
                print(f"{Barvy.BOLD}Jmeno složky> {Barvy.slozka}{Mo.nazev_slozky}{Barvy.RESET}",flush=True)
                
            
            
            stahni.close()  
            sys.stdout.flush()
            
        seznam = [] 
         
        
       
        for x in range(0, len(dec)):    
            seznam.append(dec[x]["clone_url"])            
            
        for i in range(len(seznam)):
            
            print("\t{barva}{cislo}) {hodnota}{reset}".format(barva=Barvy.BOLD,cislo=i,hodnota=seznam[i],reset=Barvy.RESET, flush=True))
            
        try:
            
            volba = input(f"{Barvy.CURSIVA}{Barvy.BOLD} čislo:")
            
            if volba.isdigit() is True:
                volba = int(volba)
                for radky in seznam[volba]:
                    sz = seznam[volba]  
                    #cesta(nazev=Mo.nazev_slozky, reposit=sz)
                cesta(nazev=Mo.nazev_slozky, reposit=sz)
            # pridani regex pro nazev_slozky developera
            # https://github.com/sivel/speedtest-cli.git
            # stred = re.search(r"/(\w+)/", url)
            # stred.group(1)
            
            elif volba.isdigit() is False:
                try:
                    vyvojar = re.search(r"/(\w+)/", volba)
                    slozka = vyvojar.group(1)
                    cesta(nazev=slozka, reposit=volba)
                except:
                    pass
            sys.stdout.flush()
        except KeyboardInterrupt:
            pass
        except ValueError:
            pass
         
            
    def posledni_verse(verse):
        with open("verze.txt", mode="r", encoding="utf-8") as autor:
            kontrola = autor.read()
            if kontrola != verse:
                return True
            else:
                return False
    def update():
        zjisti = get("https://raw.githubusercontent.com/Tobbin23/GitUb/main/verze.txt").text
    
        if Mo.posledni_verse(verse=zjisti) is True:
            
            print(f"\t{Barvy.WARNING}Probíhá update {zjisti}{Barvy.RESET}")
            
            subprocess.call(["git", "pull", "origin"])
            
        else:
            print(f"\t{Barvy.OK}Není třeba, atkuální verze je: {zjisti}{Barvy.RESET}")
            
    def lis(uprava):
        mezery = uprava.split()
        return [Mo.ret(a=x) for x in mezery]
    
