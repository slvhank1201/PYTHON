#CLASE 02
msg = """Elija una de las siguientes opciones:

a) Mostrar la suma de los dos números
b) Mostrar la resta de los dos números (el primero menos el segundo)
c) Mostrar la multiplicación de los dos números
"""
print(msg)
##obtener inputs desde teclado
numeroOne=int(input('ingrese un valor:'))
numeroTwo=int(input('ingrese segundo valor:'))
opcionMenu=input('ingrese la opcion del menu:').upper()
## Menu

print(numeroOne,numeroTwo,opcionMenu)

if(opcionMenu!='A' or opcionMenu!='B' or opcionMenu!='C'):
    if opcionMenu=='A':
        print(numeroOne+numeroTwo)
    elif opcionMenu=='B':
        print(numeroOne-numeroTwo)
    elif opcionMenu=='C':
        print(numeroOne*numeroTwo)
    else:
        print('esta opcion no es valida')
else:
    print('elija una opcion correcta')
    
    
    ### plantilla para ejercicios
    msg="""Elija una de las siguientes opciones:
Seleccione 1 para la pregunta 1    
Seleccione 2 para la pregunta 2
Seleccione 3 para la pregunta 3
Seleccione 4 para la pregunta 4
Seleccione 5 para la pregunta 5
Seleccione 5 para la pregunta 5
Seleccione 6 para la pregunta 6
Seleccione 7 para la pregunta 7
Seleccione 8 para la pregunta 8
Seleccione 9 para la pregunta 9
Seleccione 10 para la pregunta 10    
"""


vLista=[10,23,45,'hello']
vLista.append(2)
a=type(vLista[-1])

if a==str:
    print("el ultimo elemento es string")
else:
    print('el elemento no es string')
    
    
### mini sistema de notas

sistema={
    'nombreDeInstitucion':"Colegio N",
    'cursos':["python","javascript","java","php"],
    'profesores':["profesor1","profesor2"],
    'alumnos':{
        "7753":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python"],
                "notas":{}
                },
        "7754":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python","java"],
                "notas":{}
                },
        "7755":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["php"],
                "notas":{}
                },
    },
    "cursoProfesor":{
        "python":[],
        "javascript":[],
        "java":[],
        "php":[]
    }
}

##asignar profesor curso
profesoresActuales=sistema['profesores']
profesorPorAsignar=input("que profesor es: ")
if profesorPorAsignar in profesoresActuales:
    print("existe el profesor")
    print(sistema["cursos"])
    cursoPorAsignar=input("Que curso va asignar a este profesor:")
    if cursoPorAsignar in sistema['cursos']:
            cursoTemp=sistema["cursoProfesor"][cursoPorAsignar]
            cursoTemp.append(profesorPorAsignar)
            sistema['cursoProfesor'][cursoPorAsignar]=cursoTemp
    else:
        print('no existe el curso')    
else:
    print("no existe profesor,desea agregarlo")
    print(profesorPorAsignar,sistema['profesores'])
    profesorTemp=sistema['profesores']
    profesorTemp.append(profesorPorAsignar)
    sistema['profesores']=profesorTemp
    print(sistema)

## asignar nota a alumno
codAlumno=input("ingrese el codigo del alumno")
listaAlumnos=list(sistema["alumnos"].keys())
if codAlumno in listaAlumnos:
    print("alumno existe")
    cursosDelAlumno=sistema["alumnos"][codAlumno]["cursos"]
    notas=sistema["alumnos"][codAlumno]["notas"]
    notaPorIngresar=int(input("ingrese la nota por asignar"))
    sistema["alumnos"][codAlumno]["notas"]={'python':[notaPorIngresar]}
    print(sistema)
else:
    print("alumno no existe")

