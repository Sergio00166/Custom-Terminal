#code by Sergio1260

from glob import glob
from sys import path
from colors import color
from os import system as cmd

def find(arg,arg1,directory):
    if arg=="find":
        print("")
        buff1=arg1[arg1.find(" in ")+4:]
        buff=arg1[:arg1.find(" in ")]
        buff2=str(buff).split(" ")
        for x in buff2:
            if " in " in arg1:
                filepath = glob(buff1 + chr(92) + '**' + chr(92) + x, recursive=True)
            else:
                filepath = glob(directory + '**' + chr(92) + x, recursive=True)
            dest=str(filepath)[2:-2].replace(chr(92)+chr(92),chr(92))
            dest=str(dest).replace("'","")
            if not dest=="":
                print(color("   The file " + x + " is located in:", "G"))
                print(color(" " + dest,"Y"))
            else:
                print(color("  The file " + x + " doesn't exist in this directory","R"))
            print("")

    elif arg=="from":
        try:
            dic=[]
            if " in " in arg1:
                fich=arg1[:arg1.find(" in ")]
                ind=arg1[arg1.find(" in "):arg1.find(" find ")]
                if not chr(92) in ind and len(ind)==2:
                    ind=ind + chr(92)
            else:
                fich=arg1[:arg1.find(" find ")]
                ind=directory
            if " find " in arg1:
                fin=arg1[arg1.find(" find ")+6:].split(" ")
            if not ind[len(ind)-1:]==chr(92):
                ind=ind + chr(92)
            filedir=str(ind + fich).replace(chr(92)+chr(92),chr(92))
            file=open(filedir,"r")
            for x in file:
                dic.append(x)
            print("")
            for x in fin:
                x=str(x).replace('"',"").replace("'","")
                for y in dic:
                    if x in y:
                        print(" ", color(x,"B"), color("found in file:","G-"), color(filedir,"B-"),
                               color("in line:","G-"), color(str(dic.index(y)+1),"R"))
            print("")
                             
        except:
            print(color("\n  Error\n","R"))


