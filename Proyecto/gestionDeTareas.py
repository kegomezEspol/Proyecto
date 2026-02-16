import json
from datetime import datetime

# Clase Tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completado = False #Hasta que nosotros no le demos una indicacion de que ya esta completado
        # debe mantenerse en Falso (sin completar)

    def marcar_completado(self):
        self.completado = True

    def editar_tarea(self, nuevo_titulo, nueva_descripcion, nueva_fecha):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha

# Clase Usuario
class Usuario:
    def __init__(self,nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tareas(self, titulo_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo_tarea]

    def obtener_tareas(self):
        return self.tareas
        
# Clase Sistema de Gestion de tareas
class SistemaGestionTareas:
    #Inicialización del sistema de gestion de un archivo
    def __init__(self, archivo_datos = "datos_usuarios.json"):
        self.usuarios = {}
        self.archivos_datos = archivo_datos
        self.cargar_datos()

    def cargar_datos(self):
        #Cargar datos de los usuarios en JSON
        try:
            with open(self.archivos_datos, "r") as archivo:
                datos = json.load(archivo)
                for nombre_usuario, info in datos.items():
                    #Crea un objeto usuario para cada usuario en los datos
                    usuario = usuario(nombre_usuario, info["contraseña"])
                    for tarea_info in info["tareas"]:
                        #Crea un objeto tareas para cada tarea del usuario 
                        tarea = tarea(tarea_info["titulo"], tarea_info["descripcion"], tarea_info["fecha_vencimiento"])
                        tarea.completado = tarea_info["completada"]
                        usuario.agregar_tarea(tarea)
                    self.usuarios[nombre_usuario] = usuario
        except FileNotFoundError: #Manejo de excepciones
            print("Archivos de datos no encontrado, se creará uno nuevo al guardar")

        
