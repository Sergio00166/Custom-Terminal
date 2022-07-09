#code by Sergio1260

from files import files
from direct import direct
from things import things
from sizes import sizes
from find import find
from cpacut import cpacut
from other import other
from colors import color

def database(arg,arg1,directory):
    if (arg=="go" or arg=="updir" or arg=="back" or arg=="downdir"
        or arg=="dirtree" or arg=="newdir" or arg=="nodir" or arg=="contents"):
        directory=direct(arg,arg1,directory)
    elif arg=="newfile" or arg=="no" or arg=="read":
        files(arg,arg1,directory)
    elif (arg=="clear" or arg=="run" or arg=="natives"  or arg=="start"
          or arg=="ping" or arg=="tracert" or arg=="ip" or arg=="volumes"
          or arg=="repair" or arg=="cal" or arg=="time" or arg=="perform"
          or arg=="flushdns" or arg=="running" or arg=="kill"):
        things(arg,arg1,directory)
    elif arg=="dirsize" or arg=="size" or arg=="dskinfo":
        sizes(arg,arg1,directory)
    elif arg=="find" or arg=="from":
        find(arg,arg1,directory)
    elif arg=="move" or arg=="copy" or arg=="rename":
        cpacut(arg,arg1,directory)
    elif arg=="edit" or arg=="link":
        other(arg,arg1,directory)
    else:
        print(color("\n  Command not found\n","R"))
    return directory


