#code by Sergio1260

from os import system as cmd
from os import getcwd
from sys import path
from colors import color

def cpacut(arg,arg1,directory):
    tmp=str(getcwd() + chr(92) + "windows" + chr(92) + "null")
    try:
        if arg=="copy":
            to=arg1.find("to")
            if "from" in arg1:
                fro=arg1.find("from")
                fich=arg1[:fro].split()
                dest=arg1[to+3:].split()
                direct=arg1[fro+5:to]
                if not chr(92) in arg1[fro+5:to-1] and len(arg1[fro+5:to-1])==2:
                    direct=arg1[fro+5:to-1] + chr(92)
                else:
                    direct=arg1[fro+5:to-1]
                for y in dest:
                    if ":" in y and not chr(92) in y and len(y)==2:
                        y=y+chr(92)
                    for x in fich:
                        exp="copy " + direct + x + " " + direct + y
                        exp=str(exp).replace(chr(92)+chr(92),chr(92)).replace("  "," ")
                        cmd(exp + " > " + tmp)
            else:
                fich=arg1[:to].split()
                dest=arg1[to+3:].split()
                for y in dest:
                    if ":" in y and not chr(92) in y and len(y)==2:
                        y=y+chr(92)
                    for x in fich:
                        exp="copy " + directory + x + " " + y
                        exp=str(exp).replace(chr(92)+chr(92),chr(92)).replace("  "," ")
                        cmd(exp + " > " + tmp)
                        
        elif arg=="move":
            to=arg1.find("to")
            if "from" in arg1:
                fro=arg1.find("from")
                fich=arg1[:fro].split()
                if not chr(92) in arg1[fro+5:to-1] and len(arg1[fro+5:to-1])==2:
                    direct=arg1[fro+5:to-1] + chr(92)
                else:
                    direct=arg1[fro+5:to-1]
                if not chr(92) in arg1[to+3:] and len(arg1[to+3:])==2:
                    dest=arg1[to+3:] + chr(92)
                else:
                    dest=arg1[to+3:]
                for x in fich:
                    exp="MOVE " + direct + x + " " + dest
                    exp=str(exp).replace(chr(92)+chr(92),chr(92))
                    cmd(exp + " > " + tmp)
            else:
                fich=arg1[:to].split()
                dest=arg1[to+3:]
                if ":" in dest and not chr(92) in dest and len(dest)==2:
                    dest=dest+chr(92)
                for x in fich:
                    exp="MOVE " + directory + x + " " + dest
                    exp=str(exp).replace(chr(92)+chr(92),chr(92))
                    cmd(exp + " > " + tmp)

        elif arg=="rename":
            to=arg1.find("to")
            if "from" in arg1:
                fro=arg1.find("from")
                fich=arg1[:fro].split()
                dest=arg1[to+3:].split()
                if not chr(92) in arg1[fro+5:to-1] and len(arg1[fro+5:to-1])==2:
                    direct=arg1[fro+5:to-1] + chr(92)
                else:
                    direct=arg1[fro+5:to-1]
            else:
                fich=arg1[:to].split()
                dest=arg1[to+3:].split()
                direct=directory
            for x in range(0,len(fich)):
                cmd("MOVE " + direct + fich[x] + " " + direct + dest[x] + " > " + tmp)
    except:
        print(color("\n  Error\n", "R"))
            
        


