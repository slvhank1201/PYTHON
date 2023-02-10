
import os
def recursiveFunction(u:int):
    if (u==1):
        return 1
    else:
        return u+recursiveFunction(u-1)

def divideNumbers(m:int,o:int):
    a=m/o
    return a
##REQUISITO 8
def req8prob5():
 try:
    number=int(input("Ingrese un número a sumar: "))
    print("La suma de los n primeros numeros es: ",recursiveFunction(number))
    n1=int(input("Ingrese el primero numero a dividir: "))
    n2=int(input("Ingrese el segundo numero a dividir: "))
    print("La division es:",divideNumbers(n1,n2))
 except Exception as e:
    print(e)
 else:
    a=os.getcwd()
    print("este trabajo se esta ejecutando desde:",a)
 finally:
    print("PROCESO TERMINADO")