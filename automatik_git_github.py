import requests
import json
"""
https://www.datacamp.com/community/tutorials/making-http-requests-in-python
https://www.codeunderscored.com/how-to-use-json-in-python-to-access-github-api/
Vytrorit script pro jednodusi stahovani programu z github.
misto manualniho otevirani stranek a klikani na copy reposit.
Vyzada si uzivatelske jmeno a reposit daneho autora a programu.
nasledne ho potvrdi a stahne pomoci git clone <url>.
"""
username = str(input("username: "))


url = f"https://api.github.com/users/{username}/repos"

r = requests.get(url)
load = r.json()
for i in range(0, len(load)):
    print("Project number: ", i+1)
    print("====\n")
    print("reposit name: ",load[i]["description"])
    print("clone: ",load[i]["clone_url"])
    print("Language: ", load[i]["language"])
    print("reposit velikost: ",load[i]["size"]/1024,"Mb")