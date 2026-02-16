class vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

   
class Moto(vehículo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca,modelo)
        self.tipo = tipo

    def descripcion(self):
            return f"Moto {self.marca} {self.modelo}, tipo {self.tipo}"
      

mi_moto = Moto("Yamaha", "MT-B7", "Deportiva")
print(mi_moto.descripcion())