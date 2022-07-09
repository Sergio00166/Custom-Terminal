#code by Sergio1260

from os import walk
from os import stat
from os import path
from os import scandir
import psutil
from sys import path
from colors import color

def get_directory_size(directory):
    total = 0
    try:
        for entry in scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    return total

def readable(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def sizes(arg,arg1,directory):
    print("")
    if arg=="dirsize":
        if arg1=="":
            direct=directory
        else:
            if chr(92) in arg1:
                direct=arg1
            elif not chr(92)in arg1 and ":" in arg1:
                direct=arg1 + chr(92)
            else:
                direct=directory + arg1
        size=readable(get_directory_size(direct))
        print(color(" Directory: ","G") + color(direct,"B"))
        print(color(" Dir size: ","Y") + color(size,"B"))
    elif arg=="size":
        try:
            if arg1=="":
                file_size = path.getsize(directory)
            else:
                if chr(92) in arg1:
                    file_size = path.getsize(arg1)
                else:
                    file_size = path.getsize(directory + arg1)
            print('File Size:', readable(file_size))
        except:
            print(color("  Error","R"))
    elif arg=="dskinfo":
        try:
            if arg1=="":
                disk_usage = psutil.disk_usage(directory)
                print(color(" Disk ","G") + color(directory[:directory.find(chr(92))+1],"B"))
            else:
                disk_usage = psutil.disk_usage(arg1)
                print(color(" Disk ","G") + color(arg1[:arg1.find(chr(92))+1],"B"))
            print(color(" Total: ","Y-") + color(readable(disk_usage.total),"B"))
            print(color(" Free: ","Y-") + color(readable(disk_usage.free),"B"))
            print(color(" Used: ","Y-") + color(readable(disk_usage.used),"B"))
            percent=disk_usage.percent
            if percent>=75:
                percent=color(str(percent) + "%","M")
            elif percent>=50 and percent<75:
                percent=color(str(percent) + "%","R")
            elif percent>=25 and percent<50:
                percent=color(str(percent) + "%","G")
            else:
                percent=color(str(percent) + "%","B") 
            print(color(" Used percent: ","Y-") + percent)
        except:
            print(color("  Drive not found","R"))
    print("")

