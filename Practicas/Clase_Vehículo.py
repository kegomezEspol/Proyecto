class vehículo:
    contador_vehiculos = 0
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        vehículo.contador_vehiculos += 1


    def descripcion(self):
        return f"{self.marca} {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}"
   
    def conducir(self,km):
        self.kilometraje += km

    def cambiar_año(self, nuevo_año):
        if nuevo_año > self.año:
            self.año = nuevo_año
        else: 
            print("No se puede cambiar a un año anterior o igual")

    @staticmethod
    def es_moderno(año):
        return año > 2015
    
mi_auto = vehículo("Toyota", "Corolla", 2020, 15000)
print(mi_auto.descripcion())
mi_auto.conducir(100)
print(mi_auto.descripcion())
print(vehículo.es_moderno(2018))


