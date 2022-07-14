#code by Sergio1260

from os import system as cmd
from platform import system
from sys import path
from threading import Thread as thr
from time import sleep as delay
from os import getcwd

version="pre-alfa v0.0.6.7"

dirt=getcwd()
path[5]=(dirt + chr(92) + "import")
import keyboard
from colors import color
from extbanner import main as ext
#def color(arg,arg2=""): return arg
os=system()

def revert(arg):
    exp = []
    for x in reversed(arg):
        exp.append(x)
    return exp

def clear():
    global os
    if os == "Windows":
        keyboard.press_and_release('Esc')
    else:
        keyboard.press_and_release('Ctrl + U')

def init():
    global directory , database , os
    print(color(" Custom terminal by Sergio1260 ", "G"))
    if os == "Windows":
        path.append(dirt + chr(92) + 'windows')
        print(" " + color(version, "R") + color(" on ", "G") + color("Windows OS", "B"))
        directory = "C:" + chr(92)
    elif os == "Linux":
        path.append(dirt + chr(92) + 'unix')
        print(" " + color(version, "R") + color(" on ", "G") + color("Linux OS", "Y"))
        directory = chr(92)
    from database import database

def selector():
    global buffer , som , extfx , fix
    consel = 1
    fix=False
    som = False
    extfx = True
    buffer = []
    while extfx==True:
        if som==True and not len(buffer) == 0:
            if keyboard.read_key() == "flecha abajo":
                if not consel == 0 or fix==True:
                    clear()
                    if len(buffer) == 1 or fix==True:
                        keyboard.write(buffer[0])
                        fix=False
                    else:
                        consel -= 1
                        keyboard.write(buffer[consel])
            if keyboard.read_key() == "flecha arriba":
                if not consel == len(buffer)-1:
                    clear()
                    if len(buffer) == 1:
                        keyboard.write(buffer[0])
                    else:
                        consel += 1
                        keyboard.write(buffer[consel])
                fix=False
            if len(buffer) >= 8:
                contfix = 0
                tmpbuff = []
                for x in buffer:
                    if not contfix == 8:
                        tmpbuff.append(x)
                        contfix += 1
                    else:
                        buffer = []
                        for y in tmpbuff:
                            buffer.append(y)
                            tmpbuff = []
                        break
        else:
            delay(0.1)

def main():
    global directory , buffer , database , som, extfx , fix
    color("CODE")
    while True:
        buff = ""
        buff2 = ""
        print(" " + color(directory,"B-") + color(" >> ","G-"), end="")
        a = str(input())
        cont=0
        b=a.split(" ")
        exp=[]
        for x in b:
            if not x=="":
                exp.append(x)
        a=str(exp).replace("[","").replace("]","").replace("'","").replace(",","")
        c=str(a).replace(" ","")
        if not len(c)==0:
            for x in a:
                if not x == " " and cont==0:
                    buff+=x
                elif x == " " and cont==0:
                    cont=1
                else:
                    buff2+=x
            buffer = revert(buffer)
            buffer.append(a)
            buffer = revert(buffer)
            if buff=="exit":
                extfx=False
                database("clear","","")
                ext()
                exit()
            else:
                som = False
                directory = database(str.lower(buff),buff2,directory)
                som = True
                fix=True

if __name__ == "__main__":
    thr(target=selector).start()
    init()
    main()


