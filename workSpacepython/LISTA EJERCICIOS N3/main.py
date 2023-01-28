##1
#para el problema 5, si importo desde el archivo main, y se supone que desde el archivo
#main debo de ejecutar todos los problemas(incluyendo el problema 5), 
#no se ejecuta correctamente el problema porque se estaría creando un circulo visioso
#de importar el mismo problema5 al estar incluido en el main
#y si ejecuto el problema 5 e importo desde el archivo main, se ejecuta todos los import de todos los problemas
#lo cual cual no tendría sentido, así que lo hice al revés



#REQUISITO 1:
if __name__=="__main__":
    print("ejecutando archivo principal")
    
print("EJECUTANDO PROBLEMA2")
from problem2 import *


print("EJECUTANDO PROBLEMA3")
from problem3 import *


print("EJECUTANDO PROBLEMA4")
from problem4 import *


print("EJECUTANDO PROBEMA5")
#Importé desde problem5 todo el problema y el requisito, y quedaría tal que así:
import problem5 as prob5
##REQUISITO 8
try:
    prob5.plusNumbers
    prob5.divideNumbers
except Exception as e:
    print(e)
else:
    import os
    a=os.getcwd()
    print(a)
finally:
    print("PROCESO TERMINADO")

print("IMPRIMIENDO PROBLEMA6")
from problem6 import *


print("IMPRIMIENDO PROBLEMA7")
from problem7 import *




