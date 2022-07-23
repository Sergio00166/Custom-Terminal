from os import system as cmd
import math
from sys import modules
from time import sleep as delay

def work(arg,mode):
    for x in dir(math):
        arg=str(arg).replace(x,"math."+x)
    fic=open("tmp.py","w")
    fic.write("import math \n")
    fic.write("def operator(): \n")
    fic.write("    return ")
    fic.write(arg)
    fic.close()
    from tmp import operator
    try:
        if mode==1:
            print("  Result" , operator())
        elif mode==2:
            result = operator()
            print("  Succesful added" , result)
            return result
        else:
            1+1
    except:
        print("    Math error")
    del modules["tmp"]
    
def main():
    fix=False
    arg=""
    letters={"a":0,"b":0,"c":0,"d":0}
    while True:
        try:
            if fix==True:
                work(arg,3)
                fix=False
            else:
                arg=input("\n Operation: ")
                if not arg=="exit":
                    if "set" in arg:
                        #a=sin(12)
                        letter=arg[arg.find("set(")+4:arg.find(")")]
                        for x in letters:
                            if x==letter:
                               letters[x]=work(arg[arg.find(")")+1:],2)
                               fix=True
                    else:
                        for x in letters:
                            arg=arg.replace(x,str(letters[x]))
                        work(arg,1) 
                else:
                    print("")
                    exit()
        except:
            print("   FATAL ERROR")

if __name__=="__main__":
    print(" CLI CALCULATOR by Sergio1260")
    print(" version v0.2.0 - STABLE")
    main()

