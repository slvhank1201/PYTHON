__name__=="__main__"
import problem2 as pb2

import problem3 as pb3



n=int(input("Inrese el número a sumar: "))
def plusNumbers(n):
    a=(n*(n+1))/2
    print("La suma de los primeros n números es:",a)
plusNumbers(n)

m=int(input("Ingrese el dividendo:" ))
o=int(input("Ingrese el divisor: "))
def divideNumbers(m,o):
    a=m/o
    print("La división es: ",a)
divideNumbers(m,o)



