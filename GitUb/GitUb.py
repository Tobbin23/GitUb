from cmd import Cmd
from barvy import Barvy
from os import system
from Git import Mo


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

        Mo.se_t(jmeno=uzivate)
        
        
    def do_uset(self, konfig):
        #print(Mo.ret(a=konfig))
        
        print(Mo.lis(uprava=konfig))
    
    def do_exit(self, exit):
        Cmd(exit)
        return True
    def do_clear(self, clear):
        system("clear")

def start_GitUb():
    try:
        start = GitUb()
        start.prompt = "\033[1;31mGitUb\033[0m > "
        start.cmdloop()
    except KeyboardInterrupt as K:
        print(k)
        
    except KeyError as E:
        print(E)
 
        
   
if __name__=="__main__":
    try:
        start_GitUb()
    except KeyboardInterrupt:
        pass
    except KeyError:
        pass
