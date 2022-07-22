#code by Sergio1260

from files import files
from direct import direct
from things import things
from sizes import sizes
from find import find
from cpacut import cpacut
from other import other
from colors import color
from hwusage import hwinfo
from cal import calendar
from extras import extras

def database(arg,arg1,directory):
    if (arg=="go" or arg=="updir" or arg=="back" or arg=="downdir"
        or arg=="dirtree" or arg=="newdir" or arg=="nodir" or arg=="contents"):
        directory=direct(arg,arg1,directory)
    elif arg=="newfile" or arg=="no" or arg=="read":
        files(arg,arg1,directory)
    elif (arg=="clear" or arg=="run" or arg=="natives"  or arg=="start"
          or arg=="ping" or arg=="tracert" or arg=="ip" or arg=="volumes"
          or arg=="repair" or arg=="time" or arg=="flushdns" or
          arg=="running" or arg=="kill" or arg=="sys"):
        things(arg,arg1,directory)
    elif arg=="dirsize" or arg=="size" or arg=="dskinfo":
        sizes(arg,arg1,directory)
    elif arg=="find" or arg=="from":
        find(arg,arg1,directory)
    elif arg=="move" or arg=="copy" or arg=="rename":
        cpacut(arg,arg1,directory)
    elif arg=="edit" or arg=="link" or arg=="calc":
        other(arg,arg1,directory)
    elif arg=="speedtest":
        extras(arg,arg1,directory)
    elif arg=="perform":
        hwinfo(arg1)
    elif arg=="cal":
        calendar(arg1)
    else:
        print(color("\n  Command not found\n","R"))
    return directory


