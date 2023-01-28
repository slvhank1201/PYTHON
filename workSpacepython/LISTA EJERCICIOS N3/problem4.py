class CatálogoyPoducto:
    def __init__(self, lubricantes, baterías, repuestos):
        self.lubricantes=lubricantes
        self.baterías=baterías
        self.repuestos=repuestos
input1=input("Ingrese los lubricantes: ")
input2=input("Ingrese las baterías: ")
input3=input("Ingrese los repuestos: ")
catag=CatálogoyPoducto(input1,input2,input3)
def showProducts():
     print("Lubricantes: ",catag.lubricantes)
     print("Baterías: " ,catag.baterías)
     print("Repuestos: ",catag.repuestos)
print("EL CATÁLOGO ES: ")
showProducts()