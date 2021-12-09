import random

class Persona:
    def __init__(self, nombre="", edad=0, sexo="M", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = self.generaDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDNI(self):
        return self.dni

    def getSexo(self):
        return self.sexo

    def getPeso(self):
        return self.peso

    def getAltura(self):
        return self.altura

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setEdad(self, edad: int):
        self.edad = edad

    def setDNI(self, dni: str):
        self.DNI = dni

    def setSexo(self, sexo: str):
        self.sexo = sexo

    def setPeso(self, peso: float):
        self.peso = peso

    def setAltura(self, altura: float):
        self.altura = altura

    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 0:
            print(-1)
        elif imc == 0:
            print(0)
        else:
            print(1)

    def esMayorDeEdad(self):
        return self.edad > 18

    def toString(self):
        return f"{self.nombre}, {self.edad}, {self.dni}, {self.sexo}, {self.peso}, {self.altura}"

    def generaDNI(self):
        x = random.randint(1, 99999999)
        palabra = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return str(x) + palabra[x % 23]


persona1 = Persona("Juan", 20, "M", 80, 180)
persona2 = Persona("Jose", 25, "M")
persona3 = Persona()

print(persona1.toString())
print(persona1.calcularIMC())
print(persona2.toString())
print(persona3.toString())
