from os import getcwd
from os import system as cmd
som=str(getcwd()).split(chr(92))
ruta=som[0] + chr(92) + som[1] + chr(92)
fic=open("adminwin.cmd","w")
fic.write("@echo off \n")
fic.write("cd /D ")
fic.write(ruta + "\n")
fic.write("start /B /WAIT Terminal.py \n")
cmd("START Terminal.lnk")

