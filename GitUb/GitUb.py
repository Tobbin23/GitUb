#!/usr/bin/python3
"""
autor Tobbin23
"""
from cmd import Cmd
from barvy import Barvy
from os import system
import sys
from Git import Mo
from autor import logo_a,logo_b

class GitUb(Cmd):
    
    
    def do_set(self, uzivate ):
        
        if len(uzivate) < 0:
            return False
        elif uzivate.startswith("--help"):
            return "ZADEJ jmeno"
        
       
        
        Mo.se_t(jmeno=uzivate)
    def help_set(self):
        print("\tStahne informace z uživatelského účtu a zapíše do scraping.json")
        
    def do_uset(self, konfig=None):
        
        if konfig in "":
            Mo.ret(a=konfig)
        else:
            print(Mo.lis(uprava=konfig.lower()))
            
    
    def help_uset(self):
        print("\tvypíše získané informace: bez parametrů.\n"\
              "\tPridate-li argument <name> vypíše vse co odpovida argumentu.")
    def do_exit(self, exit):
        Cmd(exit)
        sys.stdout.flush()
        return True
    def help_exit(self):
        print("\tUkončení programu.")
        
    def do_clear(self, clear):
        system("clear")
        logo_a()
        sys.stdout.flush()
    def help_clear(self):
        print("\tSmazání obrazovky.")
        
    def do_clone(self,i:int):
        # k ceste paracovniho adresare prida slozku Reposits
        logo_b()
        Mo.clon()
        
    def help_clone(self):
        print("\tUmožní libovolné stažení so složky Reposits \n"\
              "\tčíselné označení slouží jako argument\n"\
              "\tChcete-li stahnout řádek ozn <3) https://> \n"\
              "\tpostačí stisknout klavesu 3 a stahování započne.\n"\
              "\n"\
              "\tNechceteli nic stahovat stiskněte klavesu Enter")
        
def start_GitUb():
    try:
        start = GitUb()
        start.prompt = " \033[1;96mGitUb\033[0m > "
        start.intro = logo_a()
        start.cmdloop()
    except KeyboardInterrupt as K:
        print(K)
        
    except KeyError as E:
        print(E)
 
        
   
if __name__=="__main__":
    start_GitUb()
    
