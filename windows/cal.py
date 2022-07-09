import calendar
import time
from datetime import datetime
from datetime import date
from sys import path
from colors import color

cl = calendar.TextCalendar()
datetime.now()
añoc=date.today().year
mesc=date.today().month

def colores(calendario):
    top=calendario[:calendario.find("\n")]
    days=calendario[calendario.find("\n"):calendario.find("Su")+3]
    rest=calendario[calendario.find("Su")+3:]
    print("\n" + color(top,"G") + color(days,"R") + color(rest,"Y"))

def coolyear(arg):
    calendar=""
    cal=arg.split("\n")
    for x in cal:
        if cal.index(x)==0:
            cal[cal.index(x)]=color(x,"B")
        elif (cal.index(x)==2 or cal.index(x)==11
             or cal.index(x)==20 or cal.index(x)==28):
            cal[cal.index(x)]=color(x,"G")
        elif (cal.index(x)==3 or cal.index(x)==12
             or cal.index(x)==21 or cal.index(x)==29):
            cal[cal.index(x)]=color(x,"R")
    for p in range(4,9):
        cal[p]=color(cal[p],"Y")
    for p in range(13,19):
        cal[p]=color(cal[p],"Y")
    for p in range(22,27):
        cal[p]=color(cal[p],"Y")
    for p in range(30,36):
        cal[p]=color(cal[p],"Y")
    for y in cal:
        calendar += y + "\n"
    print("\n" + calendar)

def calendar(arg1):
    global añoc, mesc, cl
    if True==True:
        if "year" in arg1 and not "month" in arg1 and not "this month" in arg1 and not "this year" in arg1:
            año=arg1[arg1.find("year")+5:]
            calendario=cl.formatyear(int(año))
            coolyear(calendario)
        elif "year" in arg1 and "month" in arg1 and not "this month" in arg1 and not "this year" in arg1:
            if arg1.find("year")<=arg1.find("month"):  
                año=arg1[arg1.find("year")+5:arg1.find("month")-1]
                mes=arg1[arg1.find("month")+6:]
            else:
                mes=arg1[arg1.find("month")+5:arg1.find("year")-1]
                año=arg1[arg1.find("year")+5:]
            calendario=cl.formatmonth(int(año),int(mes))
            colores(calendario)
        elif not "year" in arg1 and "month" in arg1 and not "this month" in arg1 and not "this year" in arg1:
            mes=arg1[arg1.find("month")+6:]
            calendario=cl.formatymonth(int(añoc),int(mes))
            print(color("\n" + calendario,"G"))
        elif "this year" in arg1 and "month" in arg1 and not "this month" in arg1:
            mes=arg1[arg1.find("month")+6:]
            calendario=cl.formatmonth(int(añoc), int(mes))
            colores(calendario)
        elif "this year" in arg1 and not "month" in arg1 and not "this month" in arg1:
            calendario=cl.formatyear(int(añoc))
            coolyear(calendario)
        elif "this month" in arg1 and not "year" in arg1 and not "this year" in arg1:
            calendario=cl.formatmonth(int(añoc),int(mesc))
            colores(calendario)
        elif "today" in arg1:
            day=datetime.today().strftime('%d')
            calendario=cl.formatmonth(int(añoc), int(mesc))
            calendario=str(calendario).replace(day,color(day, "By"))
            colores(calendario) 
        elif "year" in arg1 and "this month" in arg1 and not "this year" in arg1:
            if arg1.find("year")<=arg1.find("this month"):  
                año=arg1[arg1.find("year")+5:arg1.find("this month")-1]
            else:
                año=arg1[arg1.find("year")+5:]
            calendario=cl.formatmonth(int(año), int(mesc))
            colores(calendario)
        else:
            print(color("\n  Bad syntax","R"))
    else:
        print(color("\n  Bad syntax","R"))

        


    
    
