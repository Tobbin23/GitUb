import os
import sys

def cesta(nazev:str, reposit:str):
	
	sjednoceni = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Reposits",nazev)
	
	
	if os.path.exists(os.path.join(sjednoceni)):
		pp = os.chdir(sjednoceni)
		print("ok")
		# po kontrole souboru bude stahovat 
		
		down = os.system(" {path} & git clone {git}".format(path=pp,git=reposit))
		sys.stdout.flush()
	else:
		# slozka nebyla nalezena, vytvorise a stazeni probehne 
		os.mkdir(os.path.join(sjednoceni))
		pp = os.chdir(sjednoceni)
		print("byl vytroven..")  
		down = os.system(" {path} & git clone {git}".format(path=pp,git=reposit))
		sys.stdout.flush()
				