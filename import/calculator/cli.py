from os import system as cmd
import math

def work(arg):
    for x in dir(math):
        arg=str(arg).replace(x,"math."+x)
    fic=open("tmp.py","w")
    fic.write("import math \n")
    fic.write("def operator(): \n")
    fic.write("    print('Result:' , ")
    fic.write(arg)
    fic.write(")")
    fic.close()
    from tmp import operator
    operator()
    
def main():
    arg=""
    while True:
        print("")
        arg=input("Operation: ")
        if not arg=="exit":
            work(arg)
        else:
            print("")
            exit()

if __name__=="__main__":
    print(" CLI CALCULATOR by Sergio1260")
    main()
