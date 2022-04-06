from cmd import Cmd
from barvy import Barvy
from os import system
from Git import Mo
from autor import logo
#https://linuxconfig.org/how-to-perform-http-requests-with-python-part-2-the-request-library
class GitUb(Cmd):
    
    def do_set(self, uzivate ):
        
        if len(uzivate) < 0:
            return False
        elif uzivate.startswith("--help"):
            return "ZADEJ jmeno"
        
        
        """try:
            adresa = get(f"https://api.github.com/users/{uzivate}/repos")
            if adresa.status_code == 200:
                print("Spojení %s %d " % (Barvy.OK, adresa.status_code))
                load = adresa.json()
                for i in range(0, len(load)):
                    #for k, v in load[i].items():
                    Mo.zbernice_(zbernice=f"{Barvy.BLUE}{loadi}")                    
    
        except ConnectionAbortedError as f:
            print(f)"""
       
        #GitUb.do_clone(clone=uzivate)
        Mo.se_t(jmeno=uzivate)
        
        
    def do_uset(self, konfig):
        #print(Mo.ret(a=konfig))
        if konfig in "":
            Mo.ret(a="")
        else:
            print(Mo.lis(uprava=konfig))
            #Mo.nazev_slozky.append(konfig)
    
    def do_exit(self, exit):
        Cmd(exit)
        return True
    def do_clear(self, clear):
        system("clear")
        
        
    def do_clone(self,cislo:int):
        # k ceste paracovniho adresare prida slozku Reposits
        if not cislo:
            Mo.clon()
        
        
def start_GitUb():
    try:
        start = GitUb()
        start.prompt = "\033[1;31mGitUb\033[0m > "
        start.intro = logo()
        start.cmdloop()
    except KeyboardInterrupt as K:
        print(K)
        
    except KeyError as E:
        print(E)
 
        
def config(**kwargs):
    print(kwargs)    
if __name__=="__main__":
    try:
        start_GitUb()
    except KeyboardInterrupt:
        pass
    except KeyError:
        pass
