'''
class Persona:
    def __init__(self, nombre, apellido, saludo = "Hola", email = "hola@email.com"):
        self.nombre = nombre
        self.apellido = apellido
        self.saludo = saludo
        self.email = email

    print("Hola esto es la clase persona")

    def __repr__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Saludo: {self.saludo}, Email: {self.email}"
    
    def mostrarDatos(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Saludo: {self.saludo}, Email: {self.email}"
    
objPersona = Persona(saludo="Hello", email="maria@email.com", apellido="Perez", nombre="Maria")
print(objPersona)
'''
import random

for i in range(1,10):
    print(random.randint(5,1000))