# Custom-Terminal
A terminal with its own simple syntax and multiplatform

Currently the basic utilities of the command line are being created
but now it only works in Windows, but in the future it will complete 
all the functions and work under windows and linux unifying the 
commands of both systems.

In the "import" directory are all the external libraries that 
the code needs to work and all files related to each OS are  
in a folder with its name

The commands syntax in this terminal are:

*go* dir
same as cd path
*updir* dir
go to upper directory
*back*
same as cd ..
*downdir* dir
you can go to any directory in the current path by putting only its name

*newfile* name
creates a new empty file
*newdir*
same as mkdir
*nodir* dir
deletes a dir
*no* file
deletes a file
could be used as:
newfile name name2 in dir

*read* file
prints the content of the especified file

*contents* dir
same as ls
*dirtree* dir
makes a tree of the subdirs in a especific dir

*cal* this year month x 
year x this month
year x month x
today
prints a calendar with the argguments

*time*
prints the hour

*copy* and *move*
copy fich fich1 from path to path path2

*rename* name from path to newname
renames a file

*edit* file from path
edits the specified file with the nano editor

*find* file/dir in path from 
finds the specified file/dir in the path

*from* file in path find hello
finds the word hello in the specified file

*link* lnkname in path with file in path
creates a symbolic link

*dirsize* dir
prints the size of the dir

*size* file
prints the size of the file

*clear*
clears the screen

*run* arg
runs the arg

*start* app
starts the app

*ping* ip
*tracert* ip

*ip* -all
prints the ip config

*repair*
repairs the system
(sfc, dism.exe)

*perform*
prints the use of resources

*flushdns*
clears the dns cache

*running*
prints the running process

*kill* proc
kills a process

*exit*
exits the program

*natives* command
allows to run the natives commands of the OS












