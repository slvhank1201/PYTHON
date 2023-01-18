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
        print("Comando desconocido. Vuelve a intentarlo")