#code by Sergio1260

from os import system as cmd
from os import path 
from sys import path as pth
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
                    cmd("mkdir " + exp)
                elif mode==2:
                    cmd("RD " + exp)
        else:
            dires=arg1.split()
            for x in dires:
                exp=directory + x
                exp=str(exp).replace(chr(92)+chr(92),chr(92))
                if mode==1:
                    cmd("mkdir " + exp)
                elif mode==2:
                    cmd("RD " + exp)
    except:
        print(color("\n  Error\n", "R"))

def direct(arg,arg1,directory):
    olddir=directory
    if arg=="newdir": extra(1,arg1,directory)
    elif arg=="nodir": extra(2,arg1,directory)
    elif arg=="updir":
        directory=(str(directory) + arg1 + chr(92))
    elif arg=="go":
        if not arg1=="":
            directory=str(arg1 + chr(92)).replace(chr(92)+chr(92),chr(92))
        else:
            print(color("\n  Error\n","R"))
    elif arg=="downdir":
        sep=directory.split(chr(92))
        for x in sep:
            if x==arg1:
                top=sep.index(x)
        directory=""
        for x in range(0,top+1):
            directory=directory+sep[x] + chr(92)
    elif arg=="back":
        sep=directory.split(chr(92))
        if not len(sep)==2:
            sep.pop()
            sep.pop()
            directory=(chr(92).join(sep)) + chr(92)
    elif arg=="dirtree":
        if arg1=="":
            cmd("tree " + directory)
        else:
            if chr(92) in arg1:
                 cmd("tree " + str(arg1))
            else:
                cmd("tree " + directory + chr(92) + str(arg1))
    elif arg=="contents":
        print("")
        if arg1=="" or arg==" ":
            cmd("dir " + directory)
        else:
            if chr(92) in arg1:
                 cmd("dir " + str(arg1))
            elif not chr(92) in arg1 and ":" in arg1:
                cmd("dir " + str(arg1) +chr(92))
            else:
                cmd("dir " + directory + chr(92) + str(arg1))
        print("")
    if path.isdir(directory)==True:
        return str(directory).replace(chr(92) + chr(92), chr(92))
    else:
        print(color("\n  The directory does not exist\n","R"))
        return olddir
