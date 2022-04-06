from requests import get
import json
import os
from barvy import Barvy
from spravce import cesta
#print(os.path.dirname(os.path.realpath(__file__)))
"""
vytisk .json s pouziti pandas DataFrame
https://www.educba.com/python-print-table/
return if/else https://stackoverflow.com/questions/62014493/if-statement-and-return-python
https://codereview.stackexchange.com/questions/75432/clone-github-repository-using-python
https://www.programiz.com/python-programming/nested-dictionary
https://stackoverflow.com/questions/8713596/how-to-retrieve-the-list-of-all-github-repositories-of-a-person
https://www.datacamp.com/community/tutorials/making-http-requests-in-python
https://www.codeunderscored.com/how-to-use-json-in-python-to-access-github-api/
Vytrorit script pro jednodusi stahovani programu z github.
misto manualniho otevirani stranek a klikani na copy reposit.
Vyzada si uzivatelske jmeno a reposit daneho autora a programu.
nasledne ho potvrdi a stahne pomoci git clone <url>.
"""
def funkcni():
    username = str(input("username: "))

    
    url = f"https://api.github.com/users/{username}/repos"
    repos = []
    r = get(url)
    load = r.json()
    for i in range(0, len(load)):
        
        print("Project number: ", i+1)
        print("====\n")
        print("reposit name: ",load[i]["description"])
        print("clone: ",load[i]["clone_url"])
        print("Language: ", load[i]["language"])
        print("reposit velikost: ",load[i]["size"]/1024,"Mb")
       

        
class Mo:
    #for k, v in load[i].items():
    #return f"{Barvy.BLUE}{a}{Barvy.HEAD}"    
    #slovnik = {}
    
    nazev_slozky = ""
    
    #global slk
    #slk = slovnik
    
    def se_t(jmeno):
        try:
            adresa = get(f"https://api.github.com/users/{jmeno}/repos")
            if adresa.status_code == 200:
                print("Spojení %s %d " % (Barvy.OK, adresa.status_code))
                #Mo.nazev_slozky += jmeno
                load = adresa.json()
                for i in range(0, len(load)):
                    i + 1
                    with open("test.json", mode="w", encoding="utf-8") as zapis:
                        json.dump(load, zapis, indent=True)
            """            
            else:
                print("Uživatel nebyl nalezen")
                print("Skontroluj te prosím připojeni k internetu")"""
    
        except ConnectionAbortedError as f:
            print(f)

        
    def ret(a):
        with open("test.json", mode="r", encoding="utf-8") as vypis:
            data = vypis.read()
            dec = json.loads(data)
            
            #https://from-locals.com/python-file-path/
            
            try:
                if a:
                    for i in range(0, len(dec)):
                    
                        print("\n")
                        
                        print("\t",dec[i][a])
                else:
                    for i in range(0, len(dec)):
                        
                        print("Project number: ", i+1)
                        print("====\n")
                        print("reposit name: ",dec[i]["description"])
                        print("clone: ",dec[i]["clone_url"])
                        print("Language: ", dec[i]["language"])
                        print("reposit velikost: ",dec[i]["size"]/1024,"Mb")                
            except KeyError:
                pass
                
            
    def clon(radek:int):
        with open("test.json", mode="r", encoding="utf-8") as vypis:
            data = vypis.read()
            dec = json.loads(data)
            vypis.close()
            seznam = []
            
            Mo.nazev_slozky += dec[0]["owner"]["login"]
            
            for x in range(0, len(dec)):
                seznam.append(dec[x]["clone_url"])            
            
            for i in range(len(seznam)):
                print("{cislo}) {hodnota}".format(cislo=i,hodnota=seznam[i]))
             
            try:
                volba = int(input("cisl:"))
                if volba != '' or volba != ' ':
                    for radky in seznam[volba]:
                        sz = seznam[volba]
                    cesta(nazev=Mo.nazev_slozky, reposit=sz)
            except ValueError:
                pass
            
        """
        with open("test.json", mode="r", encoding="utf-8") as vypis:
            data = vypis.read()
            dec = json.loads(data)
            vypis.close()
            for i in range(0, len(dec)):
                Mo.seznam_git(dec[i]["clone_url"])
        soubor = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Reposits")
        
            
        for soubory in os.listdir(soubor):
            # kontrola zda slozka se jmenem od funkce do_set()
            if os.path.exists(os.path.join(soubor, uzivatel)):
                print("ok")
                # po kontrole souboru bude stahovat 
                down = os.system("git clone {path} {git}".format(git=Mo.seznam_git(), path=os.path.join(soubor,uzivatel)))
            # slozka nebyla nalezena, vytvorise a stazeni probehne 
            else:
                os.mkdir(os.path.join(soubor, uzivatel))
                print("byl vytroven..")  
                down = os.system("git clone {git} {path}".format(git=" ", path=os.path.join(soubor,uzivatel)))
               """
    def lis(uprava):
        mezery = uprava.split()
        I_data = []
        return [Mo.ret(a=x) for x in mezery]
    """
    for i in range(len(uprava)):
    if len(uprava) < 1:
        print("mam jeden: ", i)
    elif len(uprava) >= 2:
        print("mam dva a vice ", i)"""
