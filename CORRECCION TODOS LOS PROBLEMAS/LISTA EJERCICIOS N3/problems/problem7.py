class Producto:
    def __init__(self, pais, lote, anio):
        self.pais=pais
        self.lote=lote
        self.anio=anio
    def __str__(self)->str:
        return f"El producto tiene las siguientes características:{self.pais}-{self.lote}-{self.anio}"
Prdt=Producto('ARGENTINA','2432','2021')
def showInfo():
    Prdt.__str__
    print(Prdt)
def showCountryandYear():
    a=Prdt.pais
    b=Prdt.anio
    print(f"El país es: {a}, y el año de fabricación es: {b}")
def problema7():
    showInfo()
    showCountryandYear()



