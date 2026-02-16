class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        area = self.ancho * self.alto
        return f"El área del rectángulo de {self.ancho} cm de ancho y {self.alto} cm de alto, el área es {area} cm2"


mi_rectangulo = Rectangulo(5, 10)
print(mi_rectangulo.calcular_area())
