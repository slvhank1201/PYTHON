class Catálogo:
    products=[]
    def __init__(self, products=[]):
        self.products=products
    def addProduct(self,add):
        self.products.append(add)
    def ShowProducts(self):
        for i,j in enumerate(self.products):
            i+=1
            print(i,j)
class Producto:
    def __init__(self,nombre,claseProducto,precio):
        self.nombre=nombre
        self.claseProducto=claseProducto
        self.precio=precio
    def __str__(self)->str:
        return f'el nombre es {self.nombre}, siendo {self.claseProducto} y costando S/{self.precio}'

def problema4():
    prod1=Producto('bateria','repuesto','s/350')
    prod2=Producto('lubricante','aplicante','s/59')
    print("EL CATÁLOGO ES: ")
    catag=Catálogo([])
    catag.addProduct(prod1)
    catag.addProduct(prod2)
    catag.ShowProducts()
