#LISTA EJERCICIOS N2
#PREGUNTA1
while True:
    print("Bienvenido")
    print("""
a)Dibujar un cuadrado
b)Identificar un múltiplo de 2
c)Identificar mayores de edad en una lista
d)Salir """)
    action1=input("Ingresar opción para llevar a cabo: ").lower()
    if action1=="a":
     size=int(input("Ingrese el tamaño del cuadrado a dibujar: "))
     print("\n")
     for i in range(0,size):
        for j in range(0,size):
             print('* ', end=" ")
        print()
    elif action1=="b":
     lista=[882, 9874, 9873, 8765, 98348]
     print("Los números múltiplos de 2 son: ")
     for i in lista:
        if i%2==0:
            print(i)
    elif action1=="c":
        listaPersonas =[['Álvaro',20], ['Guzmán',17], ['Steven',21],['Fabrizio',18]]
        print("Los mayores de edad son: ")
        for j in listaPersonas:
            if j[1]>=18:
                print(j)
    elif action1=="d":
        print("Programa finalizado. ¡Hasta luego!")
        break
    else:
        print("Comando desconocido. Vuelva a intentarlo")

#PREGUNTA2
while True:
  sistemaBiblioteca={
                'Académicos':[
                  {'titulo':'Introducción al analisis matemático','autor':'Venero','prestado':False},
                  {'titulo':'ECONOMIA','autor':'Samdelar','prestado':True}
                ],
                'Novelas':[
                  {'titulo':'La ciudad y los perros','autor':'Mario Vargas Llosa','prestado':True},
                  {'titulo':'Explico algunas cosas','autor':'Alberto Rojas','prestado':False}
                ]
}
  usuarios=['Fabrizzio','David','Jose','Ximena']
  def ObtenerCategorias():
     return list(sistemaBiblioteca.keys())
  def ObtenerLibros():
     listaLibros=[]
     for c in sistemaBiblioteca.values():
        for l in c:
           listaLibros.append((l['titulo'],l['autor']))
     return listaLibros
  
  def changeStateBook(titulo,estado):
     for c in sistemaBiblioteca.values():
        for l in c:
           if l['titulo']==titulo:
              l['prestado']==estado
              print(f'El estado del libro{titulo} ha sido cambiado.')
              return l
     return "Ese libro no existe"
  def getUsers():
     return usuarios
  print("""
  1)Obtener las categorías de los libros
  2)Obtener los nombres de los libros y autores
  3)Obtener la lista de usuarios de la biblioteca
  4)Asignar estado a un libro
  5)Salir
  """)
  accion1=input("¿Qué desea hacer?: ")
  if accion1=="1":
      print(ObtenerCategorias())
  elif accion1=="2":
     print(ObtenerLibros())
  elif accion1=="4":
     print(changeStateBook('Introducción al analisis matemático',True))
  elif accion1=="3":
     print(getUsers())
  elif accion1=="5":
     break
  else:
     print("Ese comando no existe")

#PREGUNTA3
N1=int(input("Ingrese el primer número: "))
N2=int(input("Ingrese el segundo número: "))
def MayorNum(N1, N2):
    if N1>N2:
        print("El mayor es: ",N1)
    else:
        print("El mayor es: ",N2)
MayorNum(N1,N2)

#PREGUNTA4
import sys
def ia(*args):
   for arg in args:
      print(arg)
ia(*sys.argv)