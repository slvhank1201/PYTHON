
#correcion problema 2
texto="""Lorem Ipsum es simplemenente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido de relleno estándar de las industrias desde el año 1500, cuando un impresor (nombre del T. persona que se dedica a la imprenta)
desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos espécimen."""
def textSplit():
    a=texto.split(sep=" ")
    print("aplicando split: ",a)
def textCount():
    c=texto.count("Lorem Ipsum")
    print("Lorem Ipsum",c)
def textUpperCase():
    e=texto.upper()
    print("aplicando uppercase: ",e)
def textLowerCase():
    f=texto.lower()
    print("aplicando lowercase: ", f)
def textJoin():
     lm=texto.split(sep=" ")
     print(" ".join(lm))
def textFinder():
  d=texto.find("estándar")
  print("estándar",d)

def problema2():
    textCount()
    textFinder()
    textJoin()
    textSplit()
    textLowerCase()
    textUpperCase()