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
     size=6
     for i in range(0,size):
        for j in range(0,size):
             print('* ', end=" ")
        print()
    elif action1=="b":
     lista={882, 9874, 9873, 8765, 98348}
     print("Los números múltiplos de 2 son: ")
     for i in lista:
        if i%2==0:
            print(i)
        else:
            False
    elif action1=="c":
        listaPersonas ={'Álvaro':12, 'Guzmán':17, 'Steven':21,'Fabrizio':18}
        print("Los mayores de edad son: ")
        for j,k in listaPersonas.items():
            if k>=18:
                print(j)
            else:
                False
    elif action1=="d":
        print("Programa finalizado. ¡Hasta luego!")
        break
    else:
        print("Comando desconocido. Vuelva a intentarlo")

#PREGUNTA2
while True:
  sistemaBiblioteca={
                'CategoríasLibros':["Académicos", "Novelas","Enciclopedias"],
                'AutoresLibros':["Mario Vargas LLosa","Pablo Neruda","Venero","Lumbreras","Alberto Rojas","Gustabo Samdelar"],
                'nombresLibros':["La ciudad y los perros", "Explico algunas cosas","Introducción al analisis matemático","ECONOMIA","LA ENCICLOPEDIA DE LA BIOLOGIA","EL ABC DEL ESPAÑOL"],
                'listaUsuarios':["Maria","Pepito","Jose","Rodrigo","Jessica","Juan","Pedro"]
}
  print("""
  1)Obtener las categorías de los libros
  2)Obtener los nombres de los libros y autores
  3)Obtener la lista de usuarios de la biblioteca
  4)Asignar estado a un libro
  5)Salir
  """)
  accion1=input("¿Qué desea hacer?: ")
  if accion1=="1":
    print(sistemaBiblioteca['CategoríasLibros'])
  elif accion1=="2":
    print(sistemaBiblioteca["nombresLibros"])
    print(sistemaBiblioteca["AutoresLibros"])
  elif accion1=="3":
    print(sistemaBiblioteca["listaUsuarios"])
  elif accion1=="4":
    librosSinAsignar=sistemaBiblioteca["nombresLibros"]
    librosPorAsignar=input("¿Qué libro desea asignar?: ")
    if librosPorAsignar in librosSinAsignar:
      accionLibro=input("Ingrese el estado por asignar: ")
      prestado="prestado"
      disponible="disponible"
      if accionLibro==prestado:
         sistemaBiblioteca["Libros Prestados"]=librosPorAsignar
         print(sistemaBiblioteca)
      elif accionLibro==disponible:
        sistemaBiblioteca["Libros Disponibles"]=librosPorAsignar
        print(sistemaBiblioteca)
      else:
        print("Comando desconocido")
    else:
      print("Este libro no existe.")
  elif accion1=="5":
    print("¡Hasta luego!")
    break
  else:
    print("Comando desconocido. Vuelva a intentarlo")

#PREGUNTA3
N1=int(input("Ingrese el primer número: "))
N2=int(input("Ingrese el segundo número: "))
def MayorNum(N1, N2):
    if N1>N2:
        print("El mayor es:",N1)
    elif N1<N2:
        print("El mayor es:",N2)
    else:
        N1=N2
        print("Los números son iguales")
MayorNum(N1,N2)

#PREGUNTA4
import sys
nombre_script=sys.argv[0]
cantidad_args=len(sys.argv)
def imPC(nombre_script, cantidad_args):
     print(nombre_script, cantidad_args)
imPC(nombre_script, cantidad_args)
#luego se cloca $pwd, $cd
#luego se agrega los args.


  