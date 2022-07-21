#code by Sergio1260

from os import system as cmd
from time import sleep as delay
from sys import path
from colors import color

def extra(mode,arg1,directory):
    try:
        if "in" in arg1:
            fro=arg1.find("in")
            dire=arg1[:fro].split()
            if not chr(92) in arg1[fro+3:] and len(arg1[fro+3:])==2 or not arg1[:-1]==chr(92):
                direct=arg1[fro+3:] + chr(92)
            else:
                direct=arg1[fro+3:]
            if not ":" in direct:
                direct = directory + direct
            for x in dire:
                exp=direct + x
                exp=str(exp).replace(chr(92)+chr(92),chr(92))
                if mode==1:
                    open(exp,"w")
                elif mode==2:
                    cmd("DEL /F " + exp)
        else:
            dires=arg1.split()
            for x in dires:
                exp=directory + x
                exp=str(exp).replace(chr(92)+chr(92),chr(92))
                if mode==1:
                    open(exp,"w")
                elif mode==2:
                    cmd("DEL /F " + exp)
    except:
        print(color("\n  Error\n", "R"))

def files(arg,arg1,directory):
    if arg=="newfile": extra(1,arg1,directory)  
    elif arg=="no": extra(2,arg1,directory)
    elif arg=="read":
        try:
            if "from" in arg1:
                fro=arg1.find("from")
                fich=arg1[:fro]
                if not chr(92) in arg1[fro+5:] and len(arg1[fro+5:])==2 or not arg1[:-1]==chr(92):
                    direct=arg1[fro+5:] + chr(92)
                else:
                    direct=arg1[fro+5:]
                if not ":" in direct:
                    direct = directory + direct
                exp=direct + fich
                exp=str(exp).replace(chr(92)+chr(92),chr(92))
            else:
                exp=directory + arg1
                exp=str(exp).replace(chr(92)+chr(92),chr(92))    
            cont=0
            fic=open(exp,"r")
            print("")
            for x in fic:
                cont=cont+1
                print(color("  " + str(cont) + " ","B") + color(x,"G"))     
        except:
            print(color("\n  Error\n", "R"))

