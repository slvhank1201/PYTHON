#ANTHONY TYARO SILVA MACIEL

print("PREGUNTA 1")
nombres="Nombres: Anthony Tyaro "
apellidos="Apellidos: Silva Maciel"
edad="Edad: 18 años"
numerodeCelular="Num.cel.: 902304875"
print(nombres)
print(apellidos)
print(edad)
print(numerodeCelular)


print("PREGUNTA 2")

#AREA TRIANGULO
base=5
altura=4
areaTriangulo=(base*altura)
print("El área del triángulo es: ", areaTriangulo)

#AREA CUADRADO
lado=12
areaCuadrado=(lado**2)
print("El área del cuadrado es: ", areaCuadrado)

#AREA CIRCULO
R=input("Agrega el valor del radio: ")
import math
areaCirculo=(math.pi* int (R)**2)
print("El área del circulo es: ", areaCirculo)



print("PREGUNTA 3")

aProb3=88
b=10
c=5
sumaValores=aProb3+b+c
multiplicacionValores=aProb3*b*c
divisionValores=aProb3/b/c
divisionEnteraValores=aProb3//b//c
if divisionEnteraValores==1:
    print("No se puede hacer división entera.")
print("La suma de los valores es: ", sumaValores)
print("La multiplicación de los valores es: ", multiplicacionValores)
print("La división de valores es: ", divisionValores)




print("PREGUNTA 4")

aProb4=True
print("El valor es: ", str(aProb4))
print(" el tipo de dato es: ", type(aProb4))



print("PREGUNTA 5")

import sys
variableProb5=sys.argv[0]
print("La ubicación de este trabajo es: ", variableProb5)




print("PREGUNTA 6")

variableProb6=int(input("Ingrese el valor a sumar: "))
sumaValoresProb6=0
for i in range(1,variableProb6+1):
    sumaValoresProb6=sumaValoresProb6+i
print("La suma es: ", sumaValoresProb6)



print("PREGUNTA 7")

numero1Prob7=int(input("Ingrese el primer numero: "))
numero2Prob7=int(input("Ingrese el segundo numero: "))
if numero1Prob7>numero2Prob7:
    print("El valor ", numero1Prob7, "es mayor que el valor ", numero2Prob7)
else:
    print ("El primer valor es menor, o igual que el segundo.")
if numero1Prob7==numero2Prob7:
    print("El valor ", numero1Prob7, "es igual al valor ", numero2Prob7)
else:
    print("Los valores ingresados son diferentes.")
if numero1Prob7!=numero2Prob7:
    print("El valor ", numero1Prob7, "no es igual al valor ", numero2Prob7)
else:
    print("Los valores ingresados son iguales.")
if numero1Prob7>=numero2Prob7:
    print("El valor ", numero1Prob7, "es mayor, o igual que el valor ", numero2Prob7)
else:
    print("El primer valor ingresado es menor que el segundo.")



print("PREGUNTA 8")

contt="contraseña"
cont=input("Ingrese contraseña: ")        
if contt==cont.lower():
    print("Contraseña correcta. Bienvenido")
else:
    print("Contraseña incorrecta")