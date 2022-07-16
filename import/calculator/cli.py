"""Para poder ejecutar este código es necesario Python 3.0 o superior, no vale Python 2.
Python 3 puede ser descargado mediante el enlace https://www.python.org/downloads y haciendo
click en una versión de Python 3"""
 
import math
import os
#Aquí importamos las librerías


__author__ = "HDB PROGRAMMING, modified by Sergio1260"

 
def Menu():
 
    print("                       █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print("                       █                      :: C A L C U L A D O R A ::                       █")
    print("                       █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("                       █                                                                        █")
    print("                       █  1.- Suma         2.- Resta       3.-Multiplicación   4.- División     █")
    print("                       █                                                                        █")
    print("                       █  5.- Resto        6.- Potencia    7.- Raíz Cudrada    8.- Seno         █")
    print("                       █                                                                        █")
    print("                       █  9.- Arcoseno     10.- Coseno     11.- Arcocoseno     12.- Tangente    █")
    print("                       █                                                                        █")
    print("                       █  13.- Arcotangnt  14.- M.C.M      15.- M.C.D          16.- Fibonacci   █")
    print("                       █                                                                        █")
    print("                       █  17.- Factorial   18.- Val. Abs.  19.- Versión        20.- Ayuda       █")
    print("                       █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("                       █                                                                        █")
    print("                       █             21.- Borr. Pant.   22.- Menú       23.- Salir              █")
    print("                       █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
    print("")
 
def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd
 
def mcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a, b)) * b
    return mcm
 
def cls():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
 
def Calculadora():
    
    Menu()
    opc = int(input("Selecione nº de Opción: "))
    
    while (opc >0 and opc <24):

        cls()
        Menu()
        
        if (opc==1):
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Suma es:', num1+num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 1
 
            elif Continuar == "n" or Continuar == "N":
                cls()
                Menu()
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 1
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
 
        elif(opc==2):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Resta es:',num1-num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 2
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 2
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==3):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Multiplicacion es:', num1*num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 3
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 3
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==4):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
 
            try:
              print ('La Division es:', num1/num2)
              print("")
              Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
              if Continuar == "s" or Continuar == "S":
                opc = 4
 
              elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
              else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 4
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
            except ZeroDivisionError:
              print ('No se Permite la Division Entre 0')
              print("")
              Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
              if Continuar == "s" or Continuar == "S":
                opc = 4
 
              elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
              else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 4
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==5):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('El Resto es:', num1%num2)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 5
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 5
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==6):
            print("")
            base = int(input("Ingrese Base: "))
            print("")
            exponente = int(input("Ingrese Exponente: "))
            print("")
            print('La Potencia es:', base**exponente)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 6
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 6
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==7):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            print("La raíz cuadrada de {} es {}".format(num, math.sqrt(num)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 7
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("SSelecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 7
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==8):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El seno de {} es {}".format(radianes, math.sin(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 8
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
 
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 8
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==9):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El arcoseno de {} es {}".format(radianes, math.asin(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 9
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 9
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==10):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El coseno de {} es {}".format(radianes, math.cos(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 10
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 10
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==11):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El arcocoseno de {} es {}".format(radianes, math.acos(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 11
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 11
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==12):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("La tangente de {} es {}".format(radianes, math.tan(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 12
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 12
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==13):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("La arcotangente de {} es {}".format(radianes, math.atan(radianes)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 13
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 13
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
 
        elif(opc==14):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print("El M.C.M. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcm(num1, num2)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 14
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 14
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==15):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print("El M.C.D. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcd(num1, num2)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 15
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 15
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==16):
            print("")
            fibonacci = []
            x = 0
            y = 1
            num = int(input("Numero de elementos: "))
            print("")
            for n in range(num):
                fibonacci.append(x + y)
                aux = x + y
                x = y
                y = aux
            print(fibonacci)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 16
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 16
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==17):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            try:
                print("El factorial de {} es {}".format(num, math.factorial(num)))
                print("")
                Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 17
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("SSelecione nº de Opción: "))
 
                else:
                    print("")
                    Continuar = input("Por Favor escoja(S/N): ")
 
                    if Continuar == "s" or Continuar == "S":
                        opc = 17
 
                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))
 
            except ValueError:
                print("No se Admiten Números Negativos")
                print("")
                Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 17
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("SSelecione nº de Opción: "))
 
                else:
                    print("")
                    Continuar = input("Por Favor escoja(S/N): ")
 
                    if Continuar == "s" or Continuar == "S":
                        opc = 17
 
                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==18):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            print("El valor absoluto de {} es {}".format(num, math.fabs(num)))
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 17
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("SSelecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 17
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
 
        elif(opc==19):
            print("")
            print("Calculadora Python ver. 1.5.0.2")
            print("")
            opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==20):
            print("")
            print("    ==========================MENÚ DE AYUDA=============================")
            print("    |                                                                  |")
            print("    |   1.- Creador del Software       2.- ¿Cómo escojo una opción?    |")
            print("    |                                                                  |")
            print("    |                       3.- Licencia                               |")
            print("    |                                                                  |")
            print("    ====================================================================")
            print("")
            aydopc = int(input("Selecione nº de Opción: "))
            while(aydopc > 0 and aydopc < 5):
                if(aydopc==1):
                    print("")
                    print("El creador de este programa es SOMEONE360 puede contactar con el mediante el correo tutiolinux@gmail.com")
                    print("")
                    Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
                    if Continuar == "s" or Continuar == "S":
                        print("")
                        aydopc = int(input("Selecione nº de Opción: "))
 
                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))
                        aydopc = 4
 
                    else:
                        print("")
                        Continuar = input("Por Favor escoja(S/N): ")
 
                        if Continuar == "s" or Continuar == "S":
                            print("")
                            aydopc = int(input("Selecione nº de Opción: "))
 
                        elif Continuar == "n" or Continuar == "N":
                            print("")
                            opc = int(input("Selecione nº de Opción: "))
                            aydopc = 4
 
                elif(aydopc==2):
                    print("")
                    print("Solamente tiene que poner el número que está al lado de la opción y pulsar la tecla enter")
                    print("")
                    Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
                    if Continuar == "s" or Continuar == "S":
                        print("")
                        aydopc = int(input("Selecione nº de Opción: "))
 
                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))
                        aydopc = 4
 
                    else:
                        print("")
                        Continuar = input("Por Favor escoja(S/N): ")
 
                        if Continuar == "s" or Continuar == "S":
                            print("")
                            aydopc = int(input("Selecione nº de Opción: "))
 
                        elif Continuar == "n" or Continuar == "N":
                            print("")
                            opc = int(input("Selecione nº de Opción: "))
                            aydopc = 4
 
                elif(aydopc==3):
                    print("")
                    print("Este programa puede ser redistribuido, editado o vendido libremente ya que este programa es software libre y código abierto")
                    print("")
                    Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
                    if Continuar == "s" or Continuar == "S":
                        print("")
                        aydopc = int(input("Selecione nº de Opción: "))
 
                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))
                        aydopc = 4
 
                    else:
                        print("")
                        Continuar = input("Por Favor escoja(S/N): ")
 
                        if Continuar == "s" or Continuar == "S":
                            print("")
                            aydopc = int(input("Selecione nº de Opción: "))
 
                        elif Continuar == "n" or Continuar == "N":
                            print("")
                            opc = int(input("Selecione nº de Opción: "))
                            aydopc = 4
 
                elif(aydopc==4):
                    print("")
                    aydopc = int(input("Selecione nº de Opción: "))
 
        elif(opc==21):
            cls()
            Menu()
            opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==22):
            Menu()
            opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==23):
            cls()
            print("")
            exit(0)
 
    while(opc <1 or opc >23 ):
        print("")
        print("Opción no Encontrada")
        print("")
        opc = int(input("Selecione nº de Opción: "))
 
Calculadora()


