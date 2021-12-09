class Electrodomesticos:
    def __init__(self, precioB=100,color="blanco",consumo='F',peso=5):
        if color in ("blanco", "negro", "gris", "rojo", "azul"):
            self.color=color
        self.precioB = precioB
        self.comprobarConsumoEnergetico(consumo)
        self.peso = peso

    def precioFinal(self):
        if self.consumo == 'A':
            self.precioB = self.precioB + 100
        elif self.consumo == 'B':
            self.precioB = self.precioB + 80
        elif self.consumo == 'C':
            self.precioB = self.precioB + 60
        elif self.consumo == 'D':
            self.precioB = self.precioB + 50
        elif self.consumo == 'E':
            self.precioB = self.precioB + 30
        elif self.consumo == 'F':
            self.precioB = self.precioB + 10

        if 0 < self.peso < 20:
            self.precioB = self.precioB + 10
        elif 20 < self.peso < 49:
            self.precioB = self.precioB + 50
        elif 50 < self.peso < 79:
            self.precioB = self.precioB + 80
        elif self.peso < 80:
            self.precioB = self.precioB + 100

    def comprobarConsumoEnergetico(self, letra):
        if letra in ("A","B","C","D","E","F"):
            self.consumo=letra

    def getPrecio(self):
        return self.precioB

    def getColor(self):
        return self.color

    def getConsumoElectrico(self):
        return self.consumo

    def getPeso(self):
        return self.peso


class Lavadora(Electrodomesticos):
    def __init__(self, precioB=100, color="blanco", consumo='F', peso=5, carga=5):
        Electrodomesticos.__init__(self, precioB=precioB, color=color, consumo=consumo, peso=peso)
        self.carga = carga

    def precioFinal(self):
        Electrodomesticos.precioFinal(self)
        if self.carga > 30:
            self.precioB = self.precioB + 50


class Television(Electrodomesticos):
    def __init__(self, precioB=100, color="blanco", consumo='F', peso=5, resolucion=20, fourK=False):
        Electrodomesticos.__init__(self, precioB=precioB, color=color, consumo=consumo, peso=peso)
        self.resolucion = resolucion
        self.fourK = fourK

    def precioFinal(self):
        Electrodomesticos.precioFinal(self)
        if self.resolucion > 40:
            self.precioB = self.precioB * 1.3
        if self.fourK == True:
            self.precioB = self.precioB + 50


electro = ()
electroLista = list(electro)

electroLista.insert(-1, Electrodomesticos(consumo="A", peso=15))
electroLista.insert(-1, Electrodomesticos(consumo="F", peso=30))
electroLista.insert(-1, Electrodomesticos(consumo="B", peso=60))
electroLista.insert(-1, Electrodomesticos(consumo="C", peso=90))

electroLista.insert(-1, Lavadora(consumo="E", peso=50, carga=30))
electroLista.insert(-1, Lavadora(consumo="A", peso=50, carga=60))

electroLista.insert(-1, Television(peso=20, resolucion=30))
electroLista.insert(-1, Television(peso=20, resolucion=50))

tv, lava, electro = 0, 0, 0
i = 0

for ele in electroLista:
    i += 1
    ele.precioFinal()

    if isinstance(ele, Television):
        tv += ele.precioB
    elif isinstance(ele, Lavadora):
        lava += ele.precioB
    else:
        electro += ele.precioB

print("Total de televisores: " + repr(tv))
print("Total de lavadoras: " + repr(lava))
print("Total de electrodomésticos: " + repr(electro))

print("Total: " + repr(tv+lava+electro))