#ANTHONY TYARO SILVA MACIEL

print("PREGUNTA 1")
edad=input(str("Ingrese su edad: "))
nombre1=input(str("Ingrese su nombre: "))
nombre2=input(str("Ingrese su apellido: "))
print(edad, nombre1, nombre2)

print("PREGUNTA 2")
R=int(input("Agrega el valor del radio: "))

#AREA TRIANGULO INSC.
areaTriangulo=((R/2)**2)*3*(3**0.5)
print("El área del triángulo es: ", areaTriangulo)
#AREA CUADRADO INSC.
areaCuadrado=(R**2)*2
print("El área del cuadrado es: ", areaCuadrado)
#AREA CIRCULO
areaCirculo=(R**2)*3.14159
print("El área del círculo es: ", areaCirculo)



print("PREGUNTA 3")

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))

sum=num1+num2+num3
multi=num1*num2*num3
rest=num1-num2-num3
div=(num1+num3)/num2
div2=(num2-num1)//num3
print("La suma de los valores es: ", sum)
print("La multiplicación de los valores es: ", multi)
print("La división de valores es: ", div)
print("La division entera de valores es: ", div2)




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

if numero1Prob7!=numero2Prob7:
    if numero1Prob7<numero2Prob7:
        print(f'El número {numero2Prob7} es mayor')
    else:
        print(f'el número {numero1Prob7} es mayor')
else:
    print("Los valores ingresados son iguales.")


print("PREGUNTA 8")

contt=input("Ingrese contraseña: ")
cont=contt.lower()      
contt2=input("Confirme la contraseña: ")
cont2=contt2.lower()
if contt!=contt2:
    print("Las contraseñas no coinciden")
else:
    print("Las contraseñas coinciden")