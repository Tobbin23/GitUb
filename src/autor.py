#!/usr/bin/python3
from .barvy import Barvy
import urllib.request
#https://github.com/4w4k3/KnockMail/blob/master/updater.py
def logo_a():
	__autor__= "Tobbin23"
	__version__= "1.7"
	print( f"""
	

	{Barvy.OK} ██████╗ ██╗████████╗██╗   ██╗██████╗ 
	██╔════╝ ██║╚══██╔══╝██║   ██║██╔══██╗
	██║  ███╗██║   ██║   ██║   ██║██████╔╝
	██║   ██║██║   ██║   ██║   ██║██╔══██╗
	╚██████╔╝██║   ██║   ╚██████╔╝██████╔╝
	╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝{Barvy.RESET} 
		{Barvy.BOLD}{Barvy.UNDLINE}Autor   | {__autor__}{Barvy.RESET}
	        {Barvy.BOLD}{Barvy.UNDLINE}Version | {__version__}{Barvy.RESET}
        __ 
	""")
def logo_b():
	print(f"""
	      {Barvy.BOLD}()(){Barvy.RESET}             ____ 
	      {Barvy.BOLD}(..){Barvy.RESET}            {Barvy.WARNING}/|o  |{Barvy.RESET}
	      {Barvy.BOLD}/\/\{Barvy.HEAD}  download{Barvy.RESET} {Barvy.WARNING}/o|  o|{Barvy.RESET}
	     {Barvy.BOLD}c\db/o.........{Barvy.RESET}{Barvy.WARNING}/o_|_o_|{Barvy.RESET}

	""")


