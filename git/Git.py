from requests import get
import json
from barvy import Barvy

"""
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
    
    #global slk
    #slk = slovnik
    def se_t(jmeno):
        try:
            adresa = get(f"https://api.github.com/users/{jmeno}/repos")
            if adresa.status_code == 200:
                print("Spojení %s %d " % (Barvy.OK, adresa.status_code))
                load = adresa.json()
                for i in range(0, len(load)):
                    i + 1
                    with open("test.json", mode="w", encoding="utf-8") as zapis:
                        json.dump(load, zapis, indent=True)
                    
    
        except ConnectionAbortedError as f:
            print(f)

        
    def ret(a):
        with open("test.json", mode="r", encoding="utf-8") as vypis:
            data = vypis.read()
            dec = json.loads(data)
            
            
            try:
                for i in range(0, len(dec)):
                    
                    print("\n")
                    print(dec[i][a])
            except KeyError:
                pass
                
        
    
    def lis(uprava):
        mezery = uprava.split()
        I_data = []
        return [Mo.ret(x) for x in mezery]