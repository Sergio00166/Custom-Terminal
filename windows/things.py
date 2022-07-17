#code by Sergio1260

from os import system as cmd
import psutil
from os import path
from os import stat
from os import scandir
from os import getcwd
from time import sleep as delay
import time
from sys import path
path.append('import/')
from colors import color
fix = " > " + getcwd() + chr(92) + "windows" + chr(92) + "null"

def things(arg,arg1,directory):
    if arg=="clear":
        cmd("CLS")
        
    elif arg=="run":
        if chr(92) in arg1 and ":" in arg1:
            sep=arg1.split(chr(92))
            sep.pop()
            buff=""
            for x in sep:
                buff = buff + (x + chr(92))
            cmd("START /B /WAIT /D " + buff + " " + str(arg1))
            buff=""
        elif chr(92) in arg1 and not ":" in arg1:
            sep=arg1.split(chr(92))
            sep.pop()
            buff=""
            for x in sep:
                buff = buff + (x + chr(92))
            cmd("START /B /WAIT /D " + directory + buff + " " + directory + str(arg1))
            buff=""
        else:
            cmd("START /B /WAIT /D " + directory + " " + directory + str(arg1))
            
    elif arg=="start":
        cmd("START " + arg1)
    elif arg=="natives":
        cmd(arg1)
    elif arg=="ping":
        cmd("PING " + arg1)
    elif arg=="tracert":
        cmd("tracert " + arg1)
    elif arg=="ip":
        if arg1=="":
            cmd("ipconfig")
        elif arg1=="-all":
            cmd("ipconfig /all")
        else:
            print("")
            print(color("  Error","R"))
    elif arg=="repair":
        cmd("START /B /WAIT sfc /scannow")
        cmd("START /B /WAIT DISM /Online /Cleanup-Image /ScanHealth")
    elif arg=="volumes":
        cmd("fsutil fsinfo drives")
    elif arg=="time":
        print(color("\n The time is: ","Y-") + color(time.strftime('%H:%M:%S', time.localtime()),"B"))
    elif arg=="flushdns":
        cmd("ipconfig /flushdns")
    elif arg=="running":
        cmd("TASKLIST")
    elif arg=="kill":
        if arg1.endswith('.exe') or arg1.endswith('.EXE' + fix):
            cmd("TASKKILL /F /IM " + arg1)
        else:
            cmd("TASKKILL /F /IM " + arg1 + ".exe" + fix)
    print("")

    
