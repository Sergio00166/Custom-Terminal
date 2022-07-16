#code by Sergio1260

from os import system as cmd
from os import getcwd
from time import sleep as delay
from sys import path
from colors import color

impht = getcwd() + chr(92) + "import" + chr(92)
gcalc = impht + "calculator\graphical" + chr(92) + "main.pyw"
clicalc = impht + "calculator" + chr(92) + "cli.py"
nano = impht + "nano.exe "

def other(arg,arg1,directory):
    if arg=="edit":
        global nano
        if not len(arg1)==0:
            if "from" in arg1:
                fro=arg1.find("from")
                fich=arg1[:fro]
                if not chr(92) in arg1[fro+5:] and len(arg1[fro+5:])==2:
                    direct=arg1[fro+5:] + chr(92)
                else:
                    direct=arg1[fro+5:]
                exp=direct + fich
                exp=str(exp).replace(chr(92)+chr(92),chr(92))
            else:
                exp=directory + arg1
            cmd("START /B /WAIT " + nano + exp)
        else:
            print(color("\n  Error\n","R"))
            
    elif arg=="link":
        # link name in dir to linked in dir
        fix = " > " + getcwd() + chr(92) + "windows" + chr(92) + "null"
        refer=arg1[arg1.find(" to ")+4:]
        if " in " in refer:
            exe = refer[:refer.find(" in ")]
            dip = refer[refer.find(" in ")+4:]
            if dip[len(dip)-1:len(dip)]==chr(92):
                dip=dip[:len(dip)-1]
            refer = dip + chr(92) + exe
        else:
            if not ":" in refer:
                refer = directory + refer
        if " in " in arg1:
            dirname=arg1[arg1.find(" in ")+3:arg1.find(" to ")]
            dirname=str(dirname).replace(chr(92)+chr(92),chr(92))
            name=arg1[:arg1.find(" in ")] + ".lnk"
        else:
            name=arg1[:arg1.find(" to ")] + ".lnk"
            dirname=directory
        if not chr(92) in refer and not ":" in refer:
            refer = directory + refer
        if dirname[len(dirname)-1:len(dirname)]==chr(92):
            dirname=dirname[:len(dirname)-1]
        refer=str(refer).replace(chr(92)+chr(92), chr(92))
        cmd('powershell New-Item -ItemType SymbolicLink -Path "' + dirname[1:]
            + '" -Name "' + name + '" -Value "' + refer + '"' + fix)

    elif arg=="calc":
        if arg1=="-GUI" or arg1=="-gui":
            cmd("START /B " + gcalc)
        elif arg1=="-cli" or arg1=="-CLI":
            cmd("START /B /WAIT " + clicalc)
        elif arg1=="":
            cmd("START /B /WAIT " + clicalc)
        else:
            print(color("\n  Bad syntax\n","R"))

