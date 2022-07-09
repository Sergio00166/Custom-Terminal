#Styles.css in pyhton :)
def color(arg,color=""):
    from sys import path
    path.append('import/')
    import colorama
    from colorama import Fore
    from colorama import Back
    from colorama import Style
    colorama.init(autoreset = True)
    if color=="B":
        return Fore.BLUE + Style.BRIGHT + arg
    elif color=="G":
        return Fore.GREEN + Style.BRIGHT + arg
    elif color=="G-":
        return Fore.GREEN + Style.DIM + arg
    elif color=="R":
        return Fore.RED + Style.BRIGHT + arg
    elif color=="Y":
        return Fore.YELLOW + Style.BRIGHT + arg
    elif color=="Y-":
        return Fore.YELLOW + Style.DIM + arg
    elif color=="M":
        return Fore.MAGENTA + Style.NORMAL + arg
    elif color=="C":
        return Fore.CYAN + Style.NORMAL + arg
    elif color=="B-":
        return Fore.BLUE + Style.NORMAL + arg
    elif color=="bW":
        return Back.CYAN + Style.BRIGHT + arg
    elif color=="By":
        return Fore.BLUE + Style.BRIGHT + arg + Fore.YELLOW + Style.BRIGHT
    elif arg=="CODE":
        print(Fore.CYAN + Style.BRIGHT)
    else:
        return arg
