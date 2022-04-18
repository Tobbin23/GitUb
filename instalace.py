import os
import subprocess

def priprava():
	priprav = os.path.dirname(os.path.realpath(__file__))
	spustitelny = "GitUb.desktop"
	if os.path.exists(spustitelny):
		instalace(spoustec=spustitelny)
	else:
		vytvor = subprocess.call(["touch", "GitUb.desktop"])
		if os.path.exists(spustitelny):
			instalace(spoustec=spustitelny)
def instalace(spoustec):
	path_1 = os.path.join(os.path.dirname(os.path.realpath(__file__)),"GitUb.py")
	path_2 = os.path.join(os.path.dirname(os.path.realpath(__file__)),"icon/icon.ico")
	
	codo = "[Desktop Entry]\n"\
		f"Icon={path_2}\n"\
		f"Exec=python3 {path_1}\n"\
		"Terminal=true\n"\
		"Type=Application\n"\
		"Categories=None\n"\
		"StartupNotify=false\n"\
		"Name[cs]=GitUb"
	with open(spoustec, mode="w") as zapis:
		zapis.write(codo)
#instalace()
priprava()
