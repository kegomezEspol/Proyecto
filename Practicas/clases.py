class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.profesion}"

    def cambiar_profesion(self, nueva_profesion):
        self.profesion = nueva_profesion


dato1 = Persona("Carlos", "18", "Ingeniero")
print(dato1.saludar())

dato1.cambiar_profesion("Programador")
print(dato1.saludar())
