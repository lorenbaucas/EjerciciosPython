class Serie:
    def __init__(self,titulo="", numTemp=3, entregado=False, genero="", creador=""):
        self.titulo = titulo
        self.numTemp = numTemp
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    def toString(self):
        return str(self.titulo + ", " + repr(self.numTemp) + ", " + repr(self.entregado) + ", " + self.genero + ", " + self.creador)


class Videojuego:
    def __init__(self, titulo="", horasEstimadas=10, entregado=False, genero="", comp=""):
        self.titulo = titulo
        self.horasEstimadas = horasEstimadas
        self.entregado = entregado
        self.genero = genero
        self.comp = comp

    def toString(self):
        return str(self.titulo + ", " + repr(self.horasEstimadas) + ", " +  repr(self.entregado) + ", " + self.genero + ", " + self.comp)


series = list()
juegos = list()

series.insert(-1, Serie(titulo="S1", numTemp=1, entregado=True))
series.insert(-1, Serie(titulo="S2", numTemp=2, entregado=True))
series.insert(-1, Serie(titulo="S3", numTemp=3, entregado=False))
series.insert(-1, Serie(titulo="S4", numTemp=2, entregado=False))
series.insert(-1, Serie(titulo="S5", numTemp=1, entregado=True))

juegos.insert(-1, Videojuego(titulo="J1", horasEstimadas=20, entregado=False))
juegos.insert(-1, Videojuego(titulo="J2", horasEstimadas=10, entregado=True))
juegos.insert(-1, Videojuego(titulo="J3", horasEstimadas=40, entregado=True))
juegos.insert(-1, Videojuego(titulo="J4", horasEstimadas=70, entregado=True))
juegos.insert(-1, Videojuego(titulo="J5", horasEstimadas=50, entregado=False))

serieMax = Serie()
juegoMax = Videojuego()

for i in series:
    if i.entregado:
        print(i.toString())
        if i.numTemp > serieMax.numTemp:
            serieMax = i

for i in juegos:
    if i.entregado:
        print(i.toString())
        if i.horasEstimadas > juegoMax.horasEstimadas:
            juegoMax=i

print("")
print("Mayor: " + str(serieMax.toString()))
print("Mayor: " + str(juegoMax.toString()))