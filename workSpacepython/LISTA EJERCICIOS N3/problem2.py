texto="""Lorem Ipsum es simplemenente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido de relleno estándar de las industrias desde el año 1500, cuando un impresor (nombre del T. persona que se dedica a la imprenta)
desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos espécimen."""
a=texto.split(sep=" ", maxsplit=33) 
c=texto.count("Lorem Ipsum")
e=texto.upper()
f=texto.lower()
print(a)
print("/".join(texto))
print("La palabra 'Lorem Ipsum' está en la posición: ",c)
d=texto.find("estándar")
print("La palabra 'estándar' se encuentra en la columna: ",d)
print(e)
print(f)
 