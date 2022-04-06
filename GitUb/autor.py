__autor__= "Tobbin23"
__version__ = 2.2
from barvy import Barvy
def logo():
	
	print( f"""
	

	{Barvy.OK} ██████╗ ██╗████████╗██╗   ██╗██████╗ 
	██╔════╝ ██║╚══██╔══╝██║   ██║██╔══██╗
	██║  ███╗██║   ██║   ██║   ██║██████╔╝
	██║   ██║██║   ██║   ██║   ██║██╔══██╗
	╚██████╔╝██║   ██║   ╚██████╔╝██████╔╝
	╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝{Barvy.RESET} 
		{Barvy.UNDLINE}Autor   | {__autor__}{Barvy.RESET}
	        {Barvy.UNDLINE}Version | {__version__}{Barvy.RESET}
	""")