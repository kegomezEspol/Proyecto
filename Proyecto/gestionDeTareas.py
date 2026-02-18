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
                        tarea.completada = tarea_info["completada"]
                        usuario.agregar_tarea(tarea)
                    self.usuarios[nombre_usuario] = usuario
        except FileNotFoundError: #Manejo de excepciones
            print("Archivos de datos no encontrado, se creará uno nuevo al guardar")

    def guardar_datos(self):
        #Guardar los datos de los usuarios en el archivo
        datos = {}
        for nombre_usuario, usuario in self.usuarios.items():
            #Organiza las tareas y la informacion del usuario en un diccionario
            datos[nombre_usuario] = {
                "contraseña":usuario.contraseña,
                "tareas": [
                    {"titulo":tarea.titulo, "descripcion":tarea.descripcion,"fecha vencimiento": tarea.fecha_vencimiento,
                     "completada": tarea.completada}
                     for tarea in usuario.tareas
                ]
             }
        with open(self.archivos_datos, "w") as archivo:
            json.dump(datos, archivo)

    def registrar_usuario(self, nombre_ususario, contraseña):
        #Registrar un nuevo usuario si el nombre de usuario no existe
         
        if nombre_ususario in self.usuarios:
            print("El nombre de usuario ya existe")
            return False
        self.usuarios[nombre_ususario] = Usuario(nombre_ususario, contraseña)
        self.guardar_datos()
        print("Usario registrado con éxito.")
        return True
    
    def iniciar_sesion(self, nombre_usuario, contrasena):
        # Inicia sesión si el usuario y la contraseña coinciden
        usuario = self.usuarios.get(nombre_usuario)
        if usuario and usuario.contraseña == contrasena:
            print("Inicio de sesión exitoso.")
            return usuario
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return None

    def menu_usuario(self, usuario):
        while True:
            print("\n1. Crear tarea")
            print("2. Ver tareas")
            print("3. Editar tarea")
            print("4. Completar tarea")
            print("5. Eliminar tarea")
            print("6. Cerrar sesión")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                titulo = input("Título de la tarea: ")
                descripcion = input("Ingresa la descripción: ")
                fecha_vencimiento = input("Fecha de vencimiento (YYY-MM-DD): ")
                tarea = Tarea(titulo, descripcion, fecha_vencimiento)
                usuario.agregar_tarea(tarea)
                self.guardar_datos()
                print("Tarea creada con éxito")
            
            elif opcion == "2":
                tareas = usuario.obtener_tareas()
                if not tareas:
                    print("No tienes tareas")
                else:
                    for idx, tarea in enumerate(tareas, start=1):
                        estado = "Completado" if tarea.completada else "Pendiente"
                        print(f"{idx}. {tarea.titulo} - {estado} (Vence: {tarea.fecha_vencimiento})")

            elif opcion == "3":
                titulo_tarea = input("Título de la tarea a editar: ")
                tarea = next((t for t in usuario.tareas if t.titulo == titulo_tarea), None)

                if tarea:
                    nuevo_titulo = input("Nuevo título: ")
                    nueva_descripcion = input("Nueva descripción: ")
                    nueva_fecha = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                    tarea.editar_tarea(nuevo_titulo, nueva_descripcion, nueva_fecha)
                    self.guardar_datos()
                    print("Tarea actualizada con éxito.")
                else:
                    print("Tarea no encontrada.")

            elif opcion == "4":
            # Marcar una tarea como completada
                titulo_tarea = input("Título de la tarea a completar: ")
                tarea = next((t for t in usuario.tareas if t.titulo == titulo_tarea), None)

                if tarea:
                    tarea.marcar_completada()
                    self.guardar_datos()
                    print("Tarea marcada como completada.")
                else:
                    print("Tarea no encontrada.")

            elif opcion == "5":
        # Eliminar una tarea
                titulo_tarea = input("Título de la tarea a eliminar: ")
                usuario.eliminar_tarea(titulo_tarea)
                self.guardar_datos()
                print("Tarea eliminada con éxito.")

            elif opcion == "6":
                # Cerrar sesión
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

 #Ejecición del sistema
if __name__ == "__main__":
    sistema = SistemaGestionTareas()

    while True:
        print("\n----- Sistema de Gestión de tareas -----")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_usuario = input("Ingrese nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            sistema.registrar_usuario(nombre_usuario, contrasena)

        elif opcion == "2":
            nombre_usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")
            usuario = sistema.iniciar_sesion(nombre_usuario, contrasena)

            if usuario:
                sistema.menu_usuario(usuario)

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")



