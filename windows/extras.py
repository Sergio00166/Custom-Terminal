from os import system as cmd
from os import getcwd

sptst = getcwd() + "\windows\extras" + chr(92) + "speedtest.exe "

def extras(arg,arg1,directory):
    global sptst
    if arg=="speedtest":
        cmd("START /B /WAIT " + sptst)
        print("")
