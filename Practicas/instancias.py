class Libro:
    def __init__(self, titulo, autor, año_de_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro {self.titulo} ha sido prestado"
        else:
            return f"El libro {self.titulo} no está disponible para el préstamo"

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            return f"El libro {self.titulo} ya estaba disponible"


class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.libros = []

    def agregar_libros(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if self.libros:
            print(f"Libros de {self.nombre}:")
            for libro in self.libros:
                print(f"- {libro.titulo} ({libro.año_de_publicacion})")
        else:
            print(f"{self.nombre} no tiene libros registrados")


class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def tomar_prestado(self, libro):
        if libro.disponible:
            libro.prestar()
            self.prestamos.append(libro)
            return f"{self.nombre} ha tomado prestado {libro.titulo}"
        else:
            return f"{libro.titulo} no está disponible"

    def devolver_libro(self, libro):
        if libro in self.prestamos:
            libro.devolver()
            self.prestamos.remove(libro)
            return f"{self.nombre} ha devuelto {libro.titulo}"
        else:
            return f"{self.nombre} no tiene el libro {libro.titulo} en su lista de préstamos"

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)

# Crear autor
autor1 = Autor("Gabriel García Márquez", "Colombia")
autor1.agregar_libros(libro1)

# Mostrar libros del autor
autor1.mostrar_libros()

# Crear miembro
miembro1 = Miembro("Juan")

# Préstamo
print(miembro1.tomar_prestado(libro1))

# Intentar prestarlo otra vez
print(miembro1.tomar_prestado(libro1))

# Devolver libro
print(miembro1.devolver_libro(libro1))
