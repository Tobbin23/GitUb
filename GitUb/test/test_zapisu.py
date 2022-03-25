import json
import sys
from requests import get
# https://stackoverflow.com/questions/64385764/how-to-assign-list-values-to-dictionary-keys
slovnik = {"a": 2, "b": 5, "c":""}
def za():
	with open("testovani.json", mode="w") as zapis:
		
		json.dump(slovnik,zapis, indent=True)
		sys.exit
def vyp(klic):
	with open("test.json", mode="r", encoding="utf-8") as vypis:
		data = vypis.read()
		dec = json.loads(data)					
		vypis.close()
		try:	
			kk = list(klic.split())
			
			print("klic", klic)
			for i in range(0, len(dec)):
				a_dic = {dec[i][klic]}
				sloucit = dict(zip(kk, a_dic))		
				print(sloucit)
				
			"""klic_c = klic.split()
			h = ''
			for s in klic:
				h = set(klic)
				h = dict(zip(h, s))
			print(h)
			klic_c= klic.split()
			M_data = []
			
			I_data = {}
			for k,v in enumerate(klic_c):
				I_data[v] = k	
		
			
			for i in range(0, len(dec)): # len([dec])
				#print(dec[i][klic], " " ,dec[i][klic])
				#slo = dict(zip(vv, vstup))
				for m in I_data.keys():
					I_data[m] = dec[i][klic]
					print(I_data)
				for s in klic_c:
					
					print(dec[i][s])"""
				
		except KeyError:
			pass




udaj = input("zadej: ").split()
for i in udaj:
	print(type(i))
	
	vyp(klic=i)


#import os
#print(os.path.dirname(os.path.realpath(__file__)))
#for i in a.split():
	#for s in enumerate(i):
		#I_data[i] = i 
#print(I_data)