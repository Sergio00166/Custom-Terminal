#code by Sergio1260

from os import system as cmd
from time import sleep as delay
from threading import Thread
from math import floor
from os import getcwd
from sys import path
import psutil
from colors import color

fix = " > " + getcwd() + chr(92) + "windows" + chr(92) + "null"

som=0
listcpu=[]

CPU=0
RAM=0
listcpu=[]
frec=0
used=0
free=0
total=0

def printer():
    global CPU, RAM, listcpu, frec
    global used, free, total
    print("")
    print("  CPU: " + val(CPU) +"%", end=" ")
    print("running @ " + str(frec) + "Mhz")
    print("")
    cont=0
    for x in listcpu:
        if cont % 2 == 0:
            print("  Core " + str(cont) + ": " + val(x),end="      ")
        else:
            print("Core " + str(cont) + ": " + val(x))
        cont=cont + 1
    print("")
    print("  RAM: " + val(RAM) + "%", end="    ")
    print("size: " + str(trunc(total,2)) + "Gb")
    print("  used: " + str(trunc(used,2)) + "Gb", end="   ")
    print("free: " + str(trunc(free,2)) + "Gb")

def fixdprt():
    global CPU, RAM, listcpu, frec
    global used, free, total
    print("")
    print("  CPU: " + str(CPU) +"%", end=" ")
    print("running @ " + str(frec) + "Mhz")
    print("")
    cont=0
    for x in listcpu:
        if cont % 2 == 0:
            print("  Core " + str(cont) + ": " + str(x),end="      ")
        else:
            print("Core " + str(cont) + ": " + str(x))
        cont=cont + 1
    print("")
    print("  RAM: " + str(RAM) + "%", end="    ")
    print("size: " + str(trunc(total,2)) + "Gb")
    print("  used: " + str(trunc(used,2)) + "Gb", end="   ")
    print("free: " + str(trunc(free,2)) + "Gb")
        
def val(arg):
    if arg>75:
        return color(str(arg),"M")
    elif arg>=50 and arg<75:
        return color(str(arg),"R")
    elif arg<=50 and not arg<25:
        return color(str(arg),"G")
    else:
        return color(str(arg),"B")

def trunc(f, n):
    return floor(f * 10 ** n) / 10 ** n

def cont():
    global CPU, RAM, listcpu, frec
    global used, free, total
    CPU=psutil.cpu_percent(percpu=False)
    listcpu=psutil.cpu_percent(percpu=True)
    frec=psutil.cpu_freq().current
    RAM=int(int(psutil.virtual_memory().used/
                psutil.virtual_memory().total*10000))/100
    used=psutil.virtual_memory().used/1024/1024/1024
    free=psutil.virtual_memory().free/1024/1024/1024
    total=psutil.virtual_memory().total/1024/1024/1024

def loop():
    global som
    while som==1:
        cmd("CLS")
        cont()
        fixdprt()
        delay(0.5)

def hwinfo(arg1):
    global som , fix
    if arg1=="-loop":
        som=1
        Thread(target=loop).start()
        cmd("pause" + fix)
        som=0
        cmd("CLS")
    elif arg1=="-gui":
        cmd("start Taskmgr")
    elif arg1=="-gui -quit":
        cmd("TASKKILL /F /IM Taskmgr.exe" + fix)
    else:
        cont()
        printer()
        print("")
        
    



