from os import getcwd
from os import system as cmd
ruta=str(getcwd())
ruta=ruta[:ruta.find(chr(92) + "import")]
fic=open("adminwin.cmd","w")
fic.write("@echo off \n")
fic.write("cd /D ")
fic.write(ruta + "\n")
fic.write("start /B /WAIT Terminal.py \n")
cmd("START Terminal.lnk")

